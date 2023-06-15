import json


class JsonData:

    @classmethod
    def get_employers(cls, filename: str = './data/employers.json'):
        result_list = []
        with open(filename, 'r') as file:
            data = json.load(file)
        for item in data:
            result_list.append((item['id'], item['name']))
        return result_list
