from flask import Flask, request

app = Flask(__name__)

@app.route('/helloworld')
def hello_world():
    return '<h1>Hello, World!<h1>'

@app.route('/add')
def add_numbers():
    # Get numbers from query parameters: /add?a=5&b=3
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return 'Please provide both "a" and "b" query parameters.', 400
    result = a + b
    return f'The sum of {a} and {b} is {result}.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)