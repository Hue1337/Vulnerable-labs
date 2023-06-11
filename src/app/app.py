from flask_session import Session
from flask import Flask, render_template, request

app = Flask(__name__)

# Simulation for database
username = 'admin'
password = 'p@ssw0rd!'

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/index.html')
def index(error=''):
    return render_template('index.html', error=error)

@app.route('/panel.html', methods=['POST'])
def panel():
    tmp_username = request.form['username']
    tmp_password = request.form['password']

    if tmp_username == username and tmp_password == password:
        return render_template('panel.html')
    else:
        return render_template('index.html', error='Invalid username or password')
    
@app.route('/change_password', methods=['POST'])
def change_password():
    current_password = request.form['current_password']
    new_password = request.form['new_password']
    confirm_password = request.form['confirm_password']

    # Sprawdź, czy bieżące hasło jest poprawne
    if current_password == current_user.password:
        # Sprawdź, czy nowe hasło i potwierdzenie są takie same
        if new_password == confirm_password:
            # Zmień hasło użytkownika
            current_user.password = new_password
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
    return render_template('change_password.html', error=error)
