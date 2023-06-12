from flask_session import Session
from flask import Flask, render_template, request, session, redirect, flash
import os
from datetime import timedelta

app = Flask(__name__)
Session(app)

# Inicjalizacja rozszerzenia  
app.permanent_session_lifetime = timedelta(hours=24)
app.config['SECRET_KEY'] = 'key'


username = 'admin'
password = 'password'



@app.route('/')
def changer():
    return render_template('/panel.html')

@app.route('/panel.html', methods=['POST', 'GET'])
def panel():
    return render_template('panel.html', passwords_match=True)

@app.route('/index.html', methods=['POST', 'GET'])
def home():
    global password
    return render_template('index.html', visible_password=password)

@app.route('/changed_password.html', methods=['POST','GET'])
def changed_password():
    global password

    new_password = request.args.get('new_password')
    confirm_password = request.args.get('confirm_password')

    if new_password == confirm_password:
        password = confirm_password
        return render_template('changed_password.html', success='Password changed successfully')
    else:
        passwords_match = False
        return render_template('panel.html', passwords_match=passwords_match)
