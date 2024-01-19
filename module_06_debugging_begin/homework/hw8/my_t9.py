"""
У нас есть кнопочный телефон (например, знаменитая Nokia 3310), и мы хотим,
чтобы пользователь мог проще отправлять СМС. Реализуем своего собственного клавиатурного помощника.

Каждой цифре телефона соответствует набор букв:
* 2 — a, b, c;
* 3 — d, e, f;
* 4 — g, h, i;
* 5 — j, k, l;
* 6 — m, n, o;
* 7 — p, q, r, s;
* 8 — t, u, v;
* 9 — w, x, y, z.

Пользователь нажимает на клавиши, например 22736368, после чего на экране печатается basement.

Напишите функцию my_t9, которая принимает на вход строку, состоящую из цифр 2–9,
и возвращает список слов английского языка, которые можно получить из этой последовательности цифр.
"""
import json
import re
from typing import List

digit_dict = {
    2: '[a-cA-C]',
    3: '[d-fD-F]',
    4: '[g-iG-I]',
    5: '[j-lJ-L]',
    6: '[m-oM-O]',
    7: '[p-sP-S]',
    8: '[t-vT-V]',
    9: '[w-zW-Z]',
}


def my_t9(input_numbers: str) -> List[str]:
    expression = []
    for number in input_numbers:
        expression += digit_dict.get(int(number))
    pattern = ''.join(expression)
    words_list = re.findall(r'\b{pattern}[ ]\b'.format(pattern=pattern),
                            *data_into_list, re.M
                            )
    return words_list


if __name__ == '__main__':
    with open('words.txt', 'r') as file:
        data = file.read()
        data_into_list = data.replace('\n', ' ').split(",")

    numbers: str = input()
    words: List[str] = my_t9(numbers)
    print(*words, sep='\n')

