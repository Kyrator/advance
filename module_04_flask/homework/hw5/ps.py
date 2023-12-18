"""
Напишите GET-эндпоинт /ps, который принимает на вход аргументы командной строки,
а возвращает результат работы команды ps с этими аргументами.
Входные значения эндпоинт должен принимать в виде списка через аргумент arg.

Например, для исполнения команды ps aux запрос будет следующим:

/ps?arg=a&arg=u&arg=x
"""
import shlex
import string
import subprocess
from typing import List

from flask import Flask, request

app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def _ps() -> str:
    arguments: List[str] = request.args.getlist("arg")
    argument_cleaned = [shlex.quote(s) for s in arguments]
    command_str = f"ps {' '.join(argument_cleaned)}"
    command = shlex.split(command_str)
    result = subprocess.run(command, capture_output=True)

    if result.returncode != 0:
        return "Something went wrong", 500

    output = result.stdout.decode()
    return string.Template("<pre>${output}</pre>").substitute(output=output)


if __name__ == "__main__":
    app.run(debug=True)
