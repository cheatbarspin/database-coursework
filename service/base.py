class Vacancy:
    """Базовый класс вакансий не требующий переопределений"""
    title: str
    salary_min: int
    salary_max: int
    employer: str
    link: str

    def __init__(self, title, salary,  employer, link, vacancy_id, employment, requirement, experience):
        """Инициализатор класса вакансий"""
        self.title = title
        self.vacancy_id = vacancy_id
        self.salary = salary
        self.employer = employer
        self.employment = employment
        self.requirement = requirement
        self.experience = experience
        self.link = link

    # Магические методы для строкового вывода в консоль, а так же для сравнения(>, <, =...)
    def __str__(self):
        return f"{self.title} в {self.employer} зп: от {self.salary_min} до {self.salary_max}"

    def __gt__(self, other) -> bool:
        return (self.salary_min + self.salary_max) / 2 > (other.salary_min + other.salary_max) / 2

    def __lt__(self, other) -> bool:
        return (self.salary_min + self.salary_max) / 2 < (other.salary_min + other.salary_max) / 2

    def __eq__(self, other) -> bool:
        return (self.salary_min + self.salary_max) / 2 == (other.salary_min + other.salary_max) / 2

    def __ge__(self, other) -> bool:
        return (self.salary_min + self.salary_max) / 2 >= (other.salary_min + other.salary_max) / 2

    def __le__(self, other) -> bool:
        return (self.salary_min + self.salary_max) / 2 <= (other.salary_min + other.salary_max) / 2

    def to_dict(self):
        """Метод для преобразования элементов класса в dict"""
        return {
            'title': self.title,
            'vacancy_id': self.vacancy_id,
            'employer': self.employer,
            'salary': self.salary or 0,
            'employment': self.employment,
            'requirement': self.requirement,
            'experience': self.experience,
            'link': self.link,
        }
