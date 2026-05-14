from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return "Sykru Login API Calisiyor!"

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    user = data.get('username')
    pas = data.get('password')
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user, pas))
        conn.commit()
        conn.close()
        return jsonify({"status": "success", "message": "Kayit Basarili!"}), 201
    except:
        return jsonify({"status": "error", "message": "Kullanici adi zaten var"}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = data.get('username')
    pas = data.get('password')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (user, pas))
    result = cursor.fetchone()
    conn.close()
    if result:
        return jsonify({"status": "success", "message": f"Hosgeldin {user}"}), 200
    return jsonify({"status": "error", "message": "Hatali Bilgiler"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
