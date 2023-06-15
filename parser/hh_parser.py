import requests
from service.abstract import Parser

from service.base import Vacancy


class HHParser(Parser):

    def __init__(self, employer_id, area=113):

        self.area = area
        self.employer_id = employer_id
        self.url = 'https://api.hh.ru/vacancies'
        self.page = 1

    def get_data(self) -> list[tuple]:
        """Запрос"""
        self.page = 1
        responce = {"items": []}
        for page in range(1, 11):
            responce_data = requests.get(
                url=self.url,
                params={
                    'per_page': 20,
                    'page': self.page,
                    'area': self.area,
                    'employer_id': self.employer_id,
                    'only_with_salary': True
                },
            )
            self.page += 1

            responce.get('items').extend(responce_data.json().get("items"))
        return self.parse(responce)

    def parse(self, data: dict) -> list[tuple]:
        answer = []
        for el in data['items']:
            salary = el.get('salary')
            if salary and salary.get('currency') == 'RUR':
                current_salary = salary.get('from') if salary.get('from') else salary.get('to')
                answer.append((int(el['id']), el['name'], int(el['employer']['id']),
                               el['experience']['name'], el['employment']['name'],
                               el['snippet']['requirement'], int(current_salary), el['alternate_url']))
                # answer.append(Vacancy(**{
                #     "title": el['name'],
                #     'vacancy_id': int(el['id']),
                #     "employer_id": int(el['employer']['id']),
                #     "experience": el['experience']['name'],
                #     "employment": el['employment']['name'],
                #     "requirement": el['snippet']['requirement'],
                #     "salary": int(current_salary),
                #     "link": el['alternate_url'],
                # })
                #               )
        return answer


# r = requests.get('https://api.hh.ru/vacancies', params={'employer_id': "4181"})
# print(r.json())
