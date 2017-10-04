from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/login', methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(reqest.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)

@app.route('/')
def index():
    return redirect(url_for('hello_world'))

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/user/<username>')
def profile(username):
    return username + '!!!!!!!'

@app.route('/html')
def htmlreturn():
    return render_template('myweb.html')

@app.route('/pg1.html')
def myhtmlreturn():
    return render_template('pg1.html')
