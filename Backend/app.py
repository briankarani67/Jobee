from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def login():
    return "You are logged in"
    


@app.route("/greet/<name>")
def get(name):
    return f"Hi {name}, Why always, you {name}?"

@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    added = f"{num1} + {num2} = {num1+num2}"
    return added

@app.route('/handle_params')
def handle():
    name = request.args['name']
    age = request.args['age']
    return f"My name is {name}, am {age} years old."



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)