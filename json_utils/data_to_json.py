import json

from parser.hh_parser import HHParser


class JsonData:

    @classmethod
    def write_to_file(cls, data, filename: str = 'db.json'):
        with open(filename, 'w') as f:
            data_dict = []
            for el in data:
                data_dict.append(el.to_dict())
            f.write(json.dumps(data_dict, indent=4, ensure_ascii=False))

    @classmethod
    def get_employers(cls, filename: str = './data/employers.json'):
        result_list = []
        with open(filename, 'r') as file:
            data = json.load(file)
        for item in data:
            result_list.append((item['id'], item['name']))
        return result_list

# j = JsonData()
# j.write_to_file('db.json')
