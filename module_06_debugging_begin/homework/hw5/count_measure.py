import datetime
import subprocess
import re


command = r'''grep '' measure_me.log'''
file_line = subprocess.run(command, shell=True, stdout=subprocess.PIPE).stdout.decode()

pattern = r'.+(?=: "Enter)'
string = file_line
start_func = re.findall(pattern, string)

pattern = r'.+(?=: "Leave)'
string = file_line
stop_func = re.findall(pattern, string)


rez = []
for time_r, time_s in zip(start_func, stop_func):
    time_start_func = datetime.datetime.strptime(time_s, '%H:%M:%S %f')
    time_stop_func = datetime.datetime.strptime(time_r, '%H:%M:%S %f')
    rez.append((time_stop_func - time_start_func).microseconds / 1000)

answer = sum(rez)/len(rez)

print(f"Среднее время выполненения функции measure_me = {answer} миллисекунд.")




