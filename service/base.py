class Vacancy:
    """Базовый класс вакансий не требующий переопределений"""
    title: str
    salary_min: int
    salary_max: int
    employer: str
    link: str

    def __init__(self, title, salary_min, salary_max, employer, link):
        """Инициализатор класса вакансий"""
        self.title = title
        self.salary_min = salary_min
        self.salary_max = salary_max
        self.employer = employer
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
            'salary_max': self.salary_max or 0,
            'salary_min': self.salary_min or 0,
            'employer': self.employer,
            'link': self.link,
        }
