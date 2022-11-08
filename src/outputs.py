import csv
import datetime as dt
import logging

from prettytable import PrettyTable

from constants import BASE_DIR, DATETIME_FORMAT


def control_output(results, cli_args):
    """Контроль вывода результатов парсинга."""
    output = cli_args.output
    if output == 'pretty':
        # Вывод данных в PrettyTable.
        pretty_output(results)
    elif output == 'file':
        # Вывод данных в файл csv.
        file_output(results, cli_args)
    else:
        # Вывод данных по умолчанию — в терминал построчно.
        default_output(results)

def default_output(results):
    """Вывод данных в терминал построчно."""
    for row in results:
        print(*row)

def pretty_output(results):
    """Вывод данных в формате PrettyTable."""
    table = PrettyTable()
    # В качестве заголовков устанавливаем первый элемент списка.
    table.field_names = results[0]
    # Выравниваем всю таблицу по левому краю.
    table.align = 'l'
    # Добавляем все строки, начиная со второй (с индексом 1).
    table.add_rows(results[1:])
    # Печатаем таблицу.
    print(table)

def file_output(results, cli_args):
    """Создание директории и запись данных в файл."""
    results_dir = BASE_DIR / 'results'
    results_dir.mkdir(exist_ok=True)
    # Получаем режим работы парсера из аргументов командной строки.
    parser_mode = cli_args.mode
    # Получаем текущие дату и время.
    now = dt.datetime.now()
    # Сохраняем текущие дату-время.
    now_formatted = now.strftime(DATETIME_FORMAT)
    # Собираем имя файла из полученных переменных:
    # «режим работы программы» + «дата и время записи» + формат (.csv).
    file_name = f'{parser_mode}_{now_formatted}.csv'
    # Получаем абсолютный путь к файлу с результатами.
    file_path = results_dir / file_name
    # Через контекстный менеджер открываем файл по сформированному ранее пути
    # в режиме записи 'w', в нужной кодировке utf-8.
    with open(file_path, 'w', encoding='utf-8') as f:
        # Создаём «объект записи» writer.
        writer = csv.writer(f, dialect='unix')
        # Передаём в метод writerows список с результатами парсинга.
        writer.writerows(results)
    logging.info(f'Файл с результатами был сохранён: {file_path}')