"""
Напишите эндпоинт, который принимает на вход код на Python (строка)
и тайм-аут в секундах (положительное число не больше 30).
Пользователю возвращается результат работы программы, а если время, отведённое на выполнение кода, истекло,
то процесс завершается, после чего отправляется сообщение о том, что исполнение кода не уложилось в данное время.
"""
import subprocess
import shlex
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired

app = Flask(__name__)


class CodeForm(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = IntegerField(default=10)


def run_python_code_in_subproccess(code: str, timeout: int):
    cmd = f'prlimit --nproc=1:1 python -c "{code}"'
    result = subprocess.Popen(
        shlex.split(cmd),
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
        )
    was_killed_by_process = False
    try:
        out, err = result.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        result.kill()
        out, err = result.communicate()
        was_killed_by_process = True
    return out.decode(), err.decode(), was_killed_by_process


@app.route('/run_code', methods=['POST'])
def run_code():
    form = CodeForm()
    if form.validate_on_submit():
        out, err, kill = run_python_code_in_subproccess(form.code.data, form.timeout.data)
        return f"Stdout: {out}, stderr: {err}, process was killed by timeout {kill}"
    return f"Bad request. Error = {form.errors}", 400


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
