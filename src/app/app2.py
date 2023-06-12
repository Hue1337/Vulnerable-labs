from flask import Flask, render_template, request, session, redirect, flash
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'kluczyk'

# Inicjalizacja rozszerzenia
app.config['SESSION_FILE_DIR'] = './.flask_session/'
app.config['SESSION_COOKIE_SECURE'] = True  # Dla sesji HTTPS
app.config['SESSION_COOKIE_HTTPONLY'] = True  # Zabezpieczenie przed atakami XSS

Session(app)

@app.route('/')
def home():
    logged_in = session.get('logged_in')
    if logged_in:
        redirect('/panel.html')
    else:
        redirect('/index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/panel.html')
def panel():
    logged_in = session.get('logged_in')
    if logged_in:
        return render_template('panel.html')
    else:
        redirect('/index.html')

@app.route('/panel.html', methods=['POST'])
def panel():
    tmp_username = request.form['username']
    tmp_password = request.form['password']

    if tmp_username == username and tmp_password == password:
        return render_template('panel.html')
    else:
        return render_template('index.html',token='', error='Invalid username or password')