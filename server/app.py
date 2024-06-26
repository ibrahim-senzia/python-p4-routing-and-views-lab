#!/usr/bin/env python3

from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter, file=sys.stdout)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    return '\n'.join(str(i)for i in range(parameter)) + '\n'
    
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    elif operation == '*':
        answer = num1 * num2
    elif operation == 'div':
        answer = num1 / num2
    elif operation == '%':
        answer = num1 % num2
    else:
        answer = 'Invalid operation'
    return str(answer)
if __name__ == '__main__':
    app.run(port=5555, debug=True)