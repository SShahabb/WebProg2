from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def get_index():
    return 'Index!'

@app.route('/hello')
def get_hello():
    return 'Hello, World!'

@app.route('/hello<name>')
def get_hello(name):
    return 'Hello, ' +name+ '!'
    return render_template('hello.html', name=name)