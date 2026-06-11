from flask import Flask

app = Flask(__name__)


@app.route('/')
def login():
    return "You are logged in"
    


@app.route("/get", methods=['GET', 'POST'])
def get():
    return 'why'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)