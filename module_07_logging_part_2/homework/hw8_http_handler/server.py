import json
from flask import Flask, request


app = Flask(__name__)
data = []

@app.route('/log', methods=['POST'])
def log():
    global data
    data = request.form

    return 'OK', 200


@app.route('/logs', methods=['GET'])
def logs():
    """
    Рендерим список полученных логов
    return: список логов обернутый в тег HTML <pre></pre>
    """
    global data
    return f'<pre>{json.dumps(data, indent=4)}</pre>'

# TODO запустить сервер
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=3000)