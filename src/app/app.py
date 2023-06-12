from flask_session import Session
from flask import Flask, render_template, request, session, redirect, flash
import os
from datetime import timedelta

app = Flask(__name__)
Session(app)

# Inicjalizacja rozszerzenia
app.config['SESSION_FILE_DIR'] = './.flask_session/'
app.config['SESSION_COOKIE_SECURE'] = True  # Dla sesji HTTPS
app.config['SESSION_COOKIE_HTTPONLY'] = True  # Zabezpieczenie przed atakami XSS
app.permanent_session_lifetime = timedelta(hours=24)
app.config['SECRET_KEY'] = 'key'


username = 'admin'
password = 'password'



@app.route('/')
def home():
    logged_in = session.get('logged_in')
    if logged_in:
        return render_template('/panel.html')
    else:
        return render_template('/index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

# @app.route('/panel.html')
# def panel():
#     logged_in = session.get('logged_in')
#     if logged_in:
#         return render_template('panel.html')
#     else:
#         redirect('/index.html')

@app.route('/panel.html', methods=['POST'])
def panel():
    logged_in = session.get('logged_in')
    if logged_in:
        return render_template('panel.html')

    else:
        tmp_username = request.form['username']
        tmp_password = request.form['password']

        if tmp_username == username and tmp_password == password:
            app.logged_in = True
            return render_template('panel.html')
        else:
            return render_template('index.html', error='Invalid username or password')

# @app.route('/changed_password.html', methods=['POST', 'GET'])
# def changed_password():
#     global password
#     if request.method == 'POST':
#         new_password = request.form['new_password']
#         confirm_password = request.form['confirm_password']

        
#         if new_password == confirm_password:
#             password = new_password
#             return render_template('changed_password.html', success='Password changed successfully')
#         else:
#             return render_template('panel.html', error='Passwords do not match')
#     else:
#         return render_template('panel.html')
    
@app.route('/changed_password.html', methods=['POST','GET'])
def changed_password():
    global password
    password_value = request.cookies.get('new_password')
    password_confirm_value = request.cookies.get('confirm_password')

    if password_value == password_confirm_value:
        password = password_value
        return render_template('changed_password.html', success='Password changed successfully')
    else:
        return render_template('panel.html', error='Passwords do not match')
