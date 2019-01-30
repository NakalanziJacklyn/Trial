from flask import Flask,render_template

trial = Flask(__name__)

@trial.route('/')
def hello_world():
    return render_template('home.html')

    @trial.route('/')
def hello_world():
    return 'This is my about page'