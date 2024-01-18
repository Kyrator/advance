"""
Ваш коллега, применив JsonAdapter из предыдущей задачи, сохранил логи работы его сайта за сутки
в файле skillbox_json_messages.log. Помогите ему собрать следующие данные:

1. Сколько было сообщений каждого уровня за сутки.
2. В какой час было больше всего логов.
3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
4. Сколько сообщений содержит слово dog.
5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
"""
import re
from typing import Dict
import shlex
import subprocess

errors_dict = ["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


def task1() -> Dict[str, int]:
    """
    1. Сколько было сообщений каждого уровня за сутки.
    @return: словарь вида {уровень: количество}
    """
    errors_amount = {}
    for error_dict in errors_dict:
        command = shlex.split(f'''grep -c '"level": "{error_dict}"' skillbox_json_messages.log''')
        line = subprocess.run(command, capture_output=True, text=True)
        errors_amount[error_dict] = int(line.stdout.strip())
    return errors_amount


def task2() -> int:
    """
    2. В какой час было больше всего логов.
    @return: час
    """
    logs_in_hours_amount = {}
    for hour in range(24):
        if hour < 10:
            command = shlex.split(fr'''grep -c '"time": "0{hour}:[0-5][0-9]:[0-5][0-9]"' skillbox_json_messages\.log''')
        else:
            command = shlex.split(fr'''grep -c '"time": "{hour}:[0-5][0-9]:[0-5][0-9]"' skillbox_json_messages\.log''')
        line = subprocess.run(command, capture_output=True, text=True)
        logs_in_hours_amount[int(line.stdout.strip())] = hour
    return logs_in_hours_amount.get(max(logs_in_hours_amount.keys()))


def task3() -> int:
    """
    3. Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00.
    @return: количество логов
    """
    command = r'''grep -c '"time": "05:[0-1][0-9].*CRITICAL"' skillbox_json_messages.log'''
    line = subprocess.run(command, shell=True, stdout=subprocess.PIPE).stdout.decode()
    return line.strip()


def task4() -> int:
    """
    4. Сколько сообщений содержат слово dog.
    @return: количество сообщений
    """
    command = r'''grep -c '\bdog\b' skillbox_json_messages.log'''
    line = subprocess.run(command, shell=True, stdout=subprocess.PIPE).stdout.decode()

    return line.strip()


def task5() -> str:
    """
    5. Какое слово чаще всего встречалось в сообщениях уровня WARNING.
    @return: слово
    """
    line_dict = {}
    command = r'''grep 'WARNING' skillbox_json_messages.log'''
    file_line = subprocess.run(command, shell=True, stdout=subprocess.PIPE).stdout.decode()
    pattern = r'(?<=message": ").*(?="})'
    string = file_line
    result = re.findall(pattern, string)
    for line_rezult in result:
        for word in line_rezult.split(" "):
            if word in line_dict:
                line_dict[word] += 1
            else:
                line_dict[word] = 1
    return max(line_dict, key=line_dict.get)


if __name__ == '__main__':

    tasks = (task1, task2, task3, task4, task5)
    for i, task_fun in enumerate(tasks, 1):
        task_answer = task_fun()
        print(f'{i}. {task_answer}')
