"""
Довольно неудобно использовать встроенный валидатор NumberRange для ограничения числа по его длине.
Создадим свой для поля phone. Создайте валидатор обоими способами.
Валидатор должен принимать на вход параметры min и max — минимальная и максимальная длина,
а также опциональный параметр message (см. рекомендации к предыдущему заданию).
"""
from typing import Any
from typing import Optional
from flask_wtf import FlaskForm
from wtforms import Field, ValidationError


def number_length(min: int, max: int, message: Optional[str] = None):
    """Функция валидоатор"""
    def _number_length(form: FlaskForm, field: Field) -> Any:
        if min > len(str(field.data)) or len(str(field.data)) > max:
            message_error = "Номер должен состоять из 10 чисел"
            raise ValidationError(message=message if message else message_error)
    return _number_length


class NumberLength:
    """Класс Валидатор"""
    def __init__(self, min: int, max: int, message: Optional[str] = None):
        self.min = min
        self.max = max
        self.message = message

    def __call__(self, form: FlaskForm, field: Field):
        if self.min <= len(str(field.data)) <= self.max:
            message_error = "Номер должен состоять из 10 чисел"
            raise ValidationError(self.message if self.message else message_error)




