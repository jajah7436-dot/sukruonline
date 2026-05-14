from flask import Flask, request, jsonify
from auth import login_user
from database import init_db

app = Flask(__name__)

# Uygulama baslarken veritabani hazir olsun
init_db()

@app.route('/')
def index():
    return "Sykru Online API Aktif!"

@app.route('/login', methods=['POST'])
def handle_login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    result = login_user(username, password)
    status_code = 200 if result["status"] == "success" else 401
    return jsonify(result), status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
