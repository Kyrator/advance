import datetime
import os
import re

from flask import Flask
import random

app = Flask(__name__)


@app.route('/hello_world')
def hello_world():
    return "Привет, мир!"


@app.route('/cars')
def cars():
    cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
    list_cars = ", ".join(cars)
    return "{car}".format(car=list_cars)


@app.route('/cats')
def cats():
    cats = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
    return random.choice(cats)


@app.route('/get_time/now')
def get_time_now():
    data = datetime.datetime.now()
    return "Точное время: {current_time}".format(current_time=data.time())


@app.route('/get_time/future')
def get_time_future():
    future_date = datetime.datetime.now() + datetime.timedelta(hours=1)
    return "Точное время через час будет {future_date}".format(future_date=future_date)


@app.route('/get_random_word')
def get_random_word():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')
    try:
        with open(BOOK_FILE, 'r') as book:
            text_book = book.read()
            list_of_words = re.findall('[a-zа-яё]+', text_book, flags=re.IGNORECASE)
        return random.choice(list_of_words)
    except TypeError:
        return "Type Error"
    except FileNotFoundError:
        return "File not found"


@app.route('/counter')
def counter():
    counter.visits += 1
    return "Количество посещений {counter}".format(counter=counter.visits)


counter.visits = 0

if __name__ == '__main__':
    app.run(debug=True)
