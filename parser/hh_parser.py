import requests
from service.abstract import Parser
from typing import Dict, List, Any


class HHParser(Parser):

    def __init__(self, text, area=113):
        self.text = text
        self.area = area
        self.url = 'https://api.hh.ru/vacancies'
        self.page = 1

    def get_data(self) -> dict[str, list[Any]]:
        """Запрос"""
        responce = {"items": []}
        for page in range(1, 11):
            responce_data = requests.get(
                url=self.url,
                params={
                    'text': self.text,
                    'per_page': 50,
                    'page': self.page,
                    'area': self.area,
                    'only_with_salary': True
                },
            )
            self.page += 1

            responce.get('items').extend(responce_data.json().get("items"))
        return responce


