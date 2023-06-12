from flask_session import Session
from flask import Flask, render_template, request, session, redirect, flash

app = Flask(__name__)
app.secret_key = 'aHVlMTMzNw=='

# Simulation for database
username = 'admin'
password = 'p@ssw0rd!'

@app.route('/')
def hello_world():
    print(session)
    if 'username' in session:
        token = 'token123'
        return redirect(f'panel.html?token={token}')
    else:
        return render_template('index.html')

@app.route('/index.html')
@app.route('/index.html?tkoen=<token>')
def index(token, error=''):
    return render_template('index.html', error=error)

@app.route('/panel.html', methods=['POST'])
def panel():
    tmp_username = request.form['username']
    tmp_password = request.form['password']

    if tmp_username == username and tmp_password == password:
        return render_template('panel.html')
    else:
        return render_template('index.html',token='', error='Invalid username or password')
    
# @app.before_request
# def check_login():
#     if (request.path != '/index.html' and request.path != '/panel.index')  and username not in session and request.path != '/static/style.css':
#         flash('You need to login first', 'error')
#         return redirect('/index.html')

@app.route('/change_password', methods=['POST', 'GET'])
def change_password():
    current_password = request.form['current_password']
    new_password = request.form['new_password']
    confirm_password = request.form['confirm_password']

    # Sprawdź, czy bieżące hasło jest poprawne
    if current_password == password:
        # Sprawdź, czy nowe hasło i potwierdzenie są takie same
        if new_password == confirm_password:
            # Zmień hasło użytkownika
            password = new_password
            # Zapisz zmiany w bazie danych

            # Przekieruj użytkownika na stronę sukcesu
            return render_template('password_changed.html')
        else:
            # Hasło i potwierdzenie nie są takie same
            error = 'New password and confirm password do not match'
    else:
        # Bieżące hasło jest nieprawidłowe
        error = 'Invalid current password'

    # Jeśli wystąpił błąd, wyświetl formularz z komunikatem o błędzie
    flash('Incorrect login or password', 'error')
    return render_template('index.html', error=error)
