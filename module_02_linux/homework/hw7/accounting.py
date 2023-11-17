"""
Реализуйте приложение для учёта финансов, умеющее запоминать, сколько денег было потрачено за день,
а также показывать затраты за отдельный месяц и за целый год.

В программе должно быть три endpoints:

/add/<date>/<int:number> — сохранение информации о совершённой в рублях трате за какой-то день;
/calculate/<int:year> — получение суммарных трат за указанный год;
/calculate/<int:year>/<int:month> — получение суммарных трат за указанные год и месяц.

Дата для /add/ передаётся в формате YYYYMMDD, где YYYY — год, MM — месяц (от 1 до 12), DD — число (от 01 до 31).
Гарантируется, что переданная дата имеет такой формат и она корректна (никаких 31 февраля).
"""
import datetime

from flask import Flask

app = Flask(__name__)

storage = {}


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    expense: int = number
    year, month, day = int(date[:4]), int(date[4:6]), int(date[6:8])
    try:
        _ = datetime.datetime(year, month, day)
        storage.setdefault(year, {}).setdefault(month, 0)
        storage[year][month] += expense
        storage.setdefault(year, {}).setdefault("total", 0)
        storage[year]['total'] += expense
        return f'Запись произведена {storage}'
    except ValueError:
        return f'Такой даты не существует. Проверьте год - {year}, месяц - {month}, день - {day}'


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    try:
        return f"{storage[year]['total']}"
    except KeyError:
        return f"{year} год пустой, заполните значения"


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    try:
        return f"{storage[year][month]}"
    except KeyError:
        return f"{month} месяц {year} года пустой, заполните значения"

if __name__ == "__main__":
    app.run(debug=True)


