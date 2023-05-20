import json

from parser.hh_parser import HHParser


class JsonData:
    list_hh = list[HHParser] = []

    def write_to_file(self, filename: str = 'db.json'):
        with open(filename, 'w') as f:
            data = self.list_hh
            data_dict = []
            for el in data:
                data_dict.append(el)
                f.write(json.dumps(data_dict, indent=4, ensure_ascii=False))


# j = JsonData()
# j.write_to_file('db.json')

