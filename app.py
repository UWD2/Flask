from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world!"

@app.route('/hi')
def home_sucka():
    return "Hi World!"

@app.route('/user/<username>')
def show_user(username):
    return "User %s" % username

@app.route('/form')
@app.route('/form/<name>')
def show_form(name=None):
    return render_template('form.html', name=name)

if (__name__ == '__main__'):
    app.run(debug = True)