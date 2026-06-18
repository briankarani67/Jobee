from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def login():
    return "You are logged in"
    
@app.route('/render')
def hello():
    return render_template('index.html')

@app.route('/brain')
def brain():
    return render_template('brain.html')

@app.route("/greet/<name>")
def get(name):
    return f"Hi {name}, Why always, you {name}?"

@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    added = f"{num1} + {num2} = {num1+num2}"
    return added

@app.route('/handle_params')
def handle():
    if 'name' in request.args.keys() and 'age' in request.args.keys():
        name = request.args['name']
        age = request.args['age']
        return f"My name is {name}, am {age} years old."
    else:
        return "There are parameters missing"



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)