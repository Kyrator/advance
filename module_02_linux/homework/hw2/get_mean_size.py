"""
Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):

$ ls -l | python3 get_mean_size.py

Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l,
а возвращает средний размер файла в каталоге.
"""

import sys


def get_mean_size(ls_output: str) -> float:
    summ_file = 0
    count = 0
    for line in ls_output:
        count += 1
        summ_file += int(line.split()[4])
    return summ_file / count


if __name__ == '__main__':
    data: list = sys.stdin.readlines()
    data = data[1:]
    if not data:
        print('Данная директория пуста или к ней нет доступа.')
    else:
        mean_size: float = get_mean_size(data)
        print(f'Средний размер файлов в данной директории: {mean_size} байт')
