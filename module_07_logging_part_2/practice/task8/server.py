from flask import Flask
from flask import Response
from flask import request
import logging
import logging.handlers
import json

app = Flask(__name__)
message = []

@app.route('/')
def hello_world():
    return 'logging server'


@app.route('/log', methods=['POST'])
def handle_log():
    global message
    message = lorequest.form
    return "OK"


@app.route('/logs', methods=['GET'])
def logs():
    """
    Рендерим список полученных логов
    return: список логов обернутый в тег HTML <pre></pre>
    """
    global message
    return f'<pre>'+'\n'.join(message)+'</pre>'


class myflt(logging.Filter):
    def filter(self, rec):
        print(rec.__dict__)
        return 1


mfl = myflt()

log1 = logging.getLogger('MTEST')
log1.setLevel(logging.DEBUG)
# rfh = logging.handlers.RotatingFileHandler('logs', 'a', maxBytes=10000000, backupCount=10)
# formatter = logging.Formatter('%(asctime)s %(name)-15s %(levelname)-8s %(message)s')
# rfh.setFormatter(formatter)
# log1.addHandler(rfh)
log1.addFilter(mfl)
log1.error("First error generated locally")
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=3500)
