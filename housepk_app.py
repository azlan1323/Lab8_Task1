from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():

    return "Welcome to HousePK Application - Login Portal"

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    print(f"Login attempt by {username}")
    return jsonify({"message": "Login successful", "user": username})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

@app.route('/dashboard')
def dashboard():
    print("Accessing dashboard")
    return "Dashboard: House listings and analytics"
