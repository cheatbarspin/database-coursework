import json

from service.base import Vacancy


class DBManager:
    data = []
    filename = None

    def __init__(self, filename):
        self.filename = filename
        self.read_from_file()

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании."""
        com_list = {}
        for el in self.data:
            if el.employer in com_list:
                com_list[el.employer] += 1
            else:
                com_list[el.employer] = 1
        return com_list

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию."""
        all_vacancies = []
        for el in self.data:
            all_vacancies.append(el)
        return all_vacancies

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям."""
        avg_salary = []
        for el in self.data:
            avg_salary.append(sum(el.salary_min + el.salary_max))

        return sum(avg_salary) / 500

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        high_salary_res = []
        for el in self.data:
            if el['salary_min'] or el['salary_max'] > self.get_avg_salary():
                high_salary_res.append(el)
        return high_salary_res

    def get_vacancies_with_keyword(self, keyword: str):
        """Получает список всех вакансий,
         в названии которых содержатся переданные в метод слова, например “python”."""
        research = []
        found = False
        for el in self.data:
            if keyword in el['title']:
                research.append(el)
                found = True
            if found:
                [print(i) for i in research]
            else:
                print('not found')

        if not found:
            print('Данные не обнаружены, попробуйте обновить')

    def read_from_file(self):
        with open(self.filename, 'r') as f:
            for el in json.loads(f.read()):
                self.data.append(Vacancy(**el))
