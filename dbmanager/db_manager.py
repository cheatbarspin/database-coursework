import json
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from service.base import Vacancy


class DBManager:
    data = []
    filename = None

    def __init__(self, filename):
        self.filename = filename
        self.read_from_file()
        self.database = 'vacancies_bd'

    def create_db(self):
        connect = psycopg2.connect(dbname='postgres', user='cheatbarspin', password=1053)
        connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connect.cursor()
        cursor.execute(f'DROP DATABASE IF EXISTS {self.database}')
        cursor.execute(f'CREATE DATABASE {self.database}')
        cursor.close()
        connect.close()

    def create_tables(self):
        connect = psycopg2.connect(dbname=self.database, user='cheatbarspin', password=1053)
        cursor = connect.cursor()
        cursor.execute("""
CREATE TABLE IF NOT EXISTS employers (
employer_id INT PRIMARY KEY,
company_name VARCHAR(50) UNIQUE NOT NULL);
            """)
        cursor.execute("""
CREATE TABLE IF NOT EXISTS vacancies (
vacancy_id INT PRIMARY KEY,
title VARCHAR(255),
employer_id INT REFERENCES employers(employer_id) NOT NULL,
experience VARCHAR(255),
employment VARCHAR(255),
requirement VARCHAR(255),
salary INT,
url VARCHAR(30));
            """)
        connect.commit()
        cursor.close()
        connect.close()

    def add_employer(self, data):
        with psycopg2.connect(dbname=self.database, user='cheatbarspin', password=1053) as conn:
            with conn.cursor() as cur:
                cur.executemany(f"""INSERT INTO employers (employer_id, company_name)
                                VALUES(%s, %s)""", data)

    def add_vacancies(self, data):
        with psycopg2.connect(dbname=self.database, user='cheatbarspin', password=1053) as conn:
            with conn.cursor() as cur:
                cur.executemany(f"""INSERT INTO vacancies (vacancy_id, title, employer_id, experience, employment, requirement, salary, url)
                                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (vacancy_id) DO NOTHING""",
                                data)

    def get_companies_and_vacancies_count(self):
        """Метод получает список всех компаний и количество вакансий у каждой компании."""
        with psycopg2.connect(dbname=self.database, user='cheatbarspin', password=1053) as conn:
            with conn.cursor() as cur:
                cur.execute(f"""SELECT company_name, COUNT(vacancy_id) FROM employers
                                INNER JOIN vacancies using(employer_id)
                                GROUP BY company_name""")
                rows = cur.fetchall()
                for row in rows:
                    print(f'Компания: {row[0]}, Количество вакансий: {row[1]}')

    def get_all_vacancies(self):
        """Метод получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию"""
        with psycopg2.connect(dbname=self.database, user='cheatbarspin', password=1053) as conn:
            with conn.cursor() as cur:
                cur.execute(f"""SELECT company_name, title, salary, url
                                FROM vacancies
                                INNER JOIN employers USING(employer_id)""")
                rows = cur.fetchall()
                for row in rows:
                    print(f'Компания: {row[0]}, Наименование вакансии: {row[1]}, З.П.: {row[2]}, url: {row[3]}')

    def get_avg_salary(self):
        """метод получает среднюю зарплату по вакансиям"""
        with psycopg2.connect(dbname=self.database, user='cheatbarspin', password=1053) as conn:
            with conn.cursor() as cur:
                cur.execute(f"""SELECT AVG(salary)
                                FROM vacancies""")
                row = cur.fetchone()

                print(f'Средняя зароботная плата всех имеющихся вакансий: {round(row[0], 2)} руб')

    def get_vacancies_with_higher_salary(self):
        """Метод получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        with psycopg2.connect(dbname=self.database, user='cheatbarspin', password=1053) as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT * FROM vacancies
                               WHERE salary > (SELECT AVG(salary) FROM vacancies)""")
                rows = cur.fetchall()
                print('Вакансии с зарплатой выше среднего')
                for row in rows:
                    print(row)

    def get_vacancies_with_keyword(self, word):
        """"Метод получает список всех вакансий, в названии которых слово"""
        with psycopg2.connect(dbname=self.database, user='cheatbarspin', password=1053) as conn:
            with conn.cursor() as cur:
                cur.execute(f"""SELECT * FROM vacancies
                                WHERE title like '%{word}%'""")
                rows = cur.fetchall()
                for row in rows:
                    print(row)

    def read_from_file(self):
        with open(self.filename, 'r') as f:
            for el in json.loads(f.read()):
                self.data.append(Vacancy(**el))
