from dbmanager.db_manager import DBManager
from json_utils.data_to_json import JsonData
from parser.hh_parser import HHParser

DBPATH = './data/db.json'


def main():
    hh = HHParser('Python')
    data = hh.get_data()
    JsonData.write_to_file(data, DBPATH)
    manager = DBManager(DBPATH)
    # print(manager.get_companies_and_vacancies_count())
    # print(manager.get_all_vacancies())
    # print(manager.get_avg_salary())
    # keyword = 'Middle'
    # manager.get_vacancies_with_keyword(keyword)
if __name__ == "__main__":
    main()
