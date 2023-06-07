from dbmanager.db_manager import DBManager
from json_utils.data_to_json import JsonData
from parser.hh_parser import HHParser

DBPATH = './data/db.json'


def main():
    manager = DBManager(DBPATH)
    manager.create_db()
    manager.create_tables()
    employers = JsonData.get_employers()
    manager.add_employer(employers)

    # for employer in employers:
    #     manager.add_employer(employer)
    #     hh = HHParser('Python', employer['id'])
    #     data = hh.get_data()
    #     manager.add_vacancies(data)

    # print(manager.get_companies_and_vacancies_count())
    # print(manager.get_all_vacancies())
    # print(manager.get_avg_salary())
    # keyword = 'Middle'
    # manager.get_vacancies_with_keyword(keyword)


if __name__ == "__main__":
    main()
