# database-coursework

Проэкт для работы с базой данных: получает вакансии по 10 выбранным компаниям, которые лежат в 'employers.json'

В папке data лежит json файл с компаниями и их id.
В папке DBManager лежит менеджер для создания базы данных, подключения, создания таблиц и дальнейшего взаимодействия с базой данных, а так же исходник sql формата.
В папке json_utils лежит специальный класс-метод, для чтения json файла.
В папке parser лежит наш настраиваемый парсер, который парсит и получает запрос с помощью библиотеки requests.
В папке service лежит абстрактный класс, служащий ввиде шаблона, если источников было бы много.

Вся логика взаимодействия с программой описана в файле main.py

 
    1. для запуск проэкта нужно установить зависимости из файла pyproject.toml
    2. Запустить файл main.py и следовать сценарию программы