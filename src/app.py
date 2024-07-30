
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "hello container from flask"


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')


# python3 -m venv env
# source env/bin/activate
# pip3 install flask uwsgi
# pip freeze > requirements.txt
# source /Users/lap01743/Downloads/WorkSpace/e-commerce_project/src/env/bin/activate
# sudo nano /etc/hosts sữa tên miền
