from abc import ABC, abstractmethod


class Parser(ABC):
    """Класс абстракций, служит в-виде шаблона,
     чтобы не забыть применить методы в парсерах разных сервисов"""
    URL: str
    params: dict

    @abstractmethod
    def get_data(self) -> dict:
        """Метод для получения списка словарей"""
        pass

