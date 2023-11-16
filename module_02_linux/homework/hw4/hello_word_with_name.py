"""
Реализуйте endpoint /hello-world/<имя>, который возвращает строку «Привет, <имя>. Хорошей пятницы!».
Вместо хорошей пятницы endpoint должен уметь желать хорошего дня недели в целом, на русском языке.

Пример запроса, сделанного в субботу:

/hello-world/Саша  →  Привет, Саша. Хорошей субботы!
"""

from flask import Flask
from datetime import datetime

app = Flask(__name__)

weekdays_tuple = ('понедельника',
                  'вторника',
                  'среды',
                  'четверга',
                  'пятницы',
                  'субботы',
                  'воскресенья')


@app.route('/hello-world/<user>')
def hello_world(user: str):
    weekday = datetime.today().weekday()
    day = weekdays_tuple[weekday]
    if weekday == 2 or weekday == 4 or weekday == 5:
        nice = 'Хорошей'
    else:
        nice = 'Хорошего'
    return f'Привет, {user}. {nice} {day}!<br>'


if __name__ == '__main__':
    app.run(debug=True)