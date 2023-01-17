# Проект парсинга PEP
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![BeautifulSoup4](https://img.shields.io/badge/-BeautifulSoup4-464646?style=flat&logo=BeautifulSoup4&logoColor=ffffff&color=043A6B)](https://www.crummy.com/software/BeautifulSoup/)
[![Prettytable](https://img.shields.io/badge/-Prettytable-464646?style=flat&logo=Prettytable&logoColor=ffffff&color=043A6B)](https://github.com/jazzband/prettytable)
[![Logging](https://img.shields.io/badge/-Logging-464646?style=flat&logo=Logging&logoColor=ffffff&color=043A6B)](https://docs.python.org/3/library/logging.html)

## Парсинг документов PEP

> Парсер собирает данные обо всех PEP документах, сравнивает статусы и записывает их в файл,
также реализованы сбор информации о статусе версий, скачивание архива с документацией и сбор ссылок о новостях в Python,
> логирует свою работу и ошибки в командную строку и файл логов.
## Технологии проекта

- Python — высокоуровневый язык программирования.
- BeautifulSoup4 - библиотека для парсинга.
- Prettytable - библиотека для удобного отображения табличных данных.
- Logging - Логирование работы и отслеживания ошибок

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/MrGorkiy/bs4_parser_pep.git
```

```
cd bs4_parser_pep
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

## Примеры команд
Выведет справку по использованию
```
python main.py pep -h
```

Создаст csv файл с таблицей из двух колонок: «Статус» и «Количество»:
```
python main.py pep -o file
```

Выводит таблицу prettytable с тремя колонками: "Ссылка на документацию", "Версия", "Статус":
```
python main.py latest-versions -o pretty 
```

Выводит ссылки в консоль на нововведения в python:
```
python main.py whats-new
```

Автор: [MrGorkiy](https://github.com/MrGorkiy)
