import requests
from service.abstract import Parser

from service.base import Vacancy


class HHParser(Parser):

    def __init__(self, text, area=113):
        self.text = text
        self.area = area
        self.url = 'https://api.hh.ru/vacancies'
        self.page = 1

    def get_data(self) -> list[Vacancy]:
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
        return self.parse(responce)

    def parse(self, data: dict) -> list[Vacancy]:
        answer = []
        for el in data['items']:
            salary = el.get('salary')
            if salary:
                answer.append(Vacancy(**{
                    "title": el['name'],
                    "employer": el['employer']['name'],
                    "salary_max": el['salary']['to'],
                    "salary_min": el['salary']['from'],
                    "link": el['alternate_url'],
                })
                              )
        return answer
