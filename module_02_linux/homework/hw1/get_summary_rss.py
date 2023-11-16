"""
С помощью команды ps можно посмотреть список запущенных процессов.
С флагами aux эта команда выведет информацию обо всех процессах, запущенных в системе.

Запустите эту команду и сохраните выданный результат в файл:

$ ps aux > output_file.txt

Столбец RSS показывает информацию о потребляемой памяти в байтах.

Напишите функцию get_summary_rss, которая на вход принимает путь до файла с результатом выполнения команды ps aux,
а возвращает суммарный объём потребляемой памяти в человекочитаемом формате.
Это означает, что ответ надо перевести в байты, килобайты, мегабайты и так далее.
"""
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_TO_OUTPUT_FILE = os.path.join(BASE_DIR, 'output_file.txt')


def get_summary_rss(ps_output_file_path: str) -> str:
    """ func open file """
    summa = 0
    try:
        with open(ps_output_file_path, 'r', encoding='UTF-8') as ps_output:
            title_dict = ps_output.readline().split()
            index_rss = title_dict.index('RSS')
            for ps_output_line in ps_output.readlines():
                rss_data = ps_output_line.split()[index_rss]
                if rss_data.isdigit():
                    summa += int(rss_data)
    except FileNotFoundError:
        print('File not found')

    size = ['Б', 'Кб', 'Мб', 'Гб', 'Тб']
    size_index = 0
    while summa > 1024:
        summa //= 1024
        size_index += 1
    return "Объем используемой памяти {summa} {size}".format(summa=summa, size=size[size_index])


if __name__ == '__main__':
    path: str = PATH_TO_OUTPUT_FILE
    summary_rss: str = get_summary_rss(path)
    print(summary_rss)
