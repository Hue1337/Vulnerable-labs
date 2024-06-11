from flask import Flask, request, render_template_string, g
import sqlite3

app = Flask(__name__)
DATABASE = 'example.db'
flaga = "WH{FAKE_FLAG_BRO}"

def initialize_db():
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        cursor.execute('INSERT INTO users (username, password) VALUES ("admin", "msfkjSGSDg385n3t4mgxc")')
        cursor.execute('INSERT INTO users (username, password) VALUES ("user", "420420msfkjSGSDg385n3t4mgxc")')
        connection.commit()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def login(username, password):
    cursor = get_db().cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = login(username, password)
        if user:
            return f"Zalogowano pomyślnie! Witaj, {user[1]}, {flaga}"
        else:
            return "Błędna nazwa użytkownika lub hasło!"
    return render_template_string('''
        <form method="post">
            <label for="username">Nazwa użytkownika:</label>
            <input type="text" name="username" id="username">
            <label for="password">Hasło:</label>
            <input type="password" name="password" id="password">
            <input type="submit" value="Zaloguj się">
        </form>
    ''')

if __name__ == '__main__':
    initialize_db()
    app.run(debug=True)
