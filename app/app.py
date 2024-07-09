from flask import Flask, render_template, jsonify
from Model.todo import Todo

app = Flask(__name__)

@app.route('/')
def index():
    message = get_hello_message()
    return render_template('index.html', api_message=message)

@app.route('/api/hello')
def hello():
    message = get_hello_message()
    return jsonify({'message': message})

@app.route('/todo/', methods=['GET'])
def get_todo():
    todo1 = Todo(description='サンプルのTODO1', deadline='2020-12-31', status='作業中')
    todo2 = Todo(description='サンプルのTODO2', deadline='2020-12-31', status='未着手')
    todos = [todo1, todo2]
    return render_template('todo.html', todos=todos)

def get_hello_message():
    return 'Hello, Flask'

if __name__ == '__main__':
    app.run(debug=True)