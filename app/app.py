from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    message = get_hello_message()
    return render_template('index.html', api_message=message)

@app.route('/api/hello')
def hello():
    message = get_hello_message()
    return jsonify({'message': message})

def get_hello_message():
    return 'Hello, Flask'

if __name__ == '__main__':
    app.run(debug=True)