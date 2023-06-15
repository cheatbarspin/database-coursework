from dbmanager.db_manager import DBManager
from json_utils.data_to_json import JsonData
from parser.hh_parser import HHParser

DBPATH = './data/db.json'


def main():
    manager = DBManager(DBPATH)
    choice_user = input("Введите 1 если хотите обновить базу данных, или введите любую клавишу: ")
    if choice_user == '1':
        manager.create_db()
        manager.create_tables()
        employers = JsonData.get_employers()
        manager.add_employer(employers)

        for employer in employers:
            print(f"{employer[1]} - Готово!")
            hh = HHParser(employer[0])
            data = hh.get_data()
            manager.add_vacancies(data)
        else:
            while True:
                print('Введите цифру согласно меню')
                print(f"""
                1. Получить список всех компаний и количество вакансий у каждой компании
                2. Получить список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
                3. Получить среднюю зарплату по вакансиям
                4. Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям
                5. получает список всех вакансий, в названии которых содержатся слово
                0. Выход из программы""")
                print()
                user_input = input('Введите цифру: ')
                if user_input == '1':
                    manager.get_companies_and_vacancies_count()
                elif user_input == '2':
                    manager.get_all_vacancies()
                elif user_input == '3':
                    manager.get_avg_salary()
                elif user_input == '4':
                    manager.get_vacancies_with_higher_salary()
                elif user_input == '5':
                    word = input('Введите слово: ')
                    manager.get_vacancies_with_keyword(word)
                elif user_input == '0':
                    break
                else:
                    print('Некорректный ввод')


if __name__ == "__main__":
    main()
