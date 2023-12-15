"""
В эндпоинт /registration добавьте все валидаторы, о которых говорилось в последнем видео:

1) email (текст, обязательно для заполнения, валидация формата);
2) phone (число, обязательно для заполнения, длина — десять символов, только положительные числа);
3) name (текст, обязательно для заполнения);
4) address (текст, обязательно для заполнения);
5) index (только числа, обязательно для заполнения);
6) comment (текст, необязательно для заполнения).
"""
import json
from urllib.parse import unquote_plus

import requests
from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import Email, InputRequired, NumberRange

from hw2_validators import number_length, NumberLength

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), NumberRange(min=1_000_000_000, max=9_999_999_999)])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired()])
    comment = StringField()


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, name, phone, address = form.email.data, form.name.data, form.phone.data, form.address.data

        return f"Successfully registered user {email} with phone +7{phone}"

    errors_list = form.errors
    print(errors_list)

    email_errors_list = form.email.errors
    print(email_errors_list)

    return f"Invalid input, {form.errors}", 400




if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
