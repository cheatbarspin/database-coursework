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

# j = JsonData()
# j.write_to_file('db.json')
