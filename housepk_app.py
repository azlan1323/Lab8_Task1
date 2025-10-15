from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to HousePK Application - Dashboard View"

@app.route('/dashboard')
def dashboard():
    print("Accessing dashboard")
    return "Dashboard: House listings and analytics"

if __name__ == '__main__':
    app.run(debug=True, port=5001)