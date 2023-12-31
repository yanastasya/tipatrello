## Tipatrello - 
### приложение по добавлению и просмотру проектов и задач в нем
##### Тестовое задание на вакансию python backend разработчик в ЦИР г.Вологда

## Оглавление
1. [Техническое описание проекта](#тз)
2. [Инструкция по развороту проекта локально](#инструкция)

<a name="тз"></a>  
## Техническое описание проекта.
Приложение по добавлению и просмотру проектов и задач в нем.</br>
В проекте может быть несколько задач и есть руководитель проекта.</br>
Каждый сотрудник одновременно может работать над несколькими задачами.</br>
Задачи создаются для каждого проекта уникальные. Задача может ветвиться на подзадачи.</br> 
Проект содержит следующую информацию: название, описание, отметка о состоянии проекта (активен / неактивен).</br>
Задача содержит следующую информацию: название, срок исполнения, описание, статус задачи (новая, в работе, закрыта).</br>
Сотрудник содержит следующую информацию: ФИО, должность.</br>
Управление записями CRUD через админпанель Django.</br>
БД заполнена и содержит 251 проектов и 10 000+ задач, 1000 сотрулников.</br>
Главная страница выводит древовидную структуру проектов со списком задач. </br>
При нажатии на название задачи открывается детальная информация о задаче со списком сотрудников, работающими над ней.</br>
На детальной странице задачи добавлена возможность написать комментарий к данной задачи. Ниже видны все ранее написанные комментарии (начиная с
последнего). Комментарий содержит следующую информацию: текст, дата
написания.</br>
[:arrow_up:Оглавление](#Оглавление)
<a name="инструкция"></a>  
## Инструкции по развороту проекта локально
1) скачать репозиторий и перейти в корневой каталог, в терминале последовательно выполнить следующие команды (для ОС Windows)
2) развернуть виртуальное окружение ```python -m venv venv```
3) активировать виртуальное окружение ```source venv/Scripts/activate```
4) установить зависимости ```pip install -r requirements.txt```
5) создать и применить миграции 
```python manage.py makemigrations projects```
```python manage.py migrate```
6) заполнить базу данными: выполнить команды (строго в данной последовательности), это может занять некоторое время:
    ```python manage.py load_workers_data```
    ```python manage.py load_projects_data```
    ```python manage.py load_tasks_data``` 
>Либо заменить файл db.sqlite3, созданный автоматически после применеия миграций на одноимённый файл из вложения к письму. 

>В базу занесены данные о 1000 сотрудниках, 10 000 задачах, 250 проектах.

7) создать суперпользователя для входа в админку
```python manage.py createsuperuser```
8)  запустить проект локально: ```python manage.py runserver```</br>
[:arrow_up:Оглавление](#Оглавление)

автор: Клинцова Анастасия Павловна
