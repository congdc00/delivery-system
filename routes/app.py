from crypt import methods
from unicodedata import name
from flask import Flask
from flask import request, redirect, url_for, render_template, session
from flask_cors import CORS, cross_origin
from application.config import TEMPLATE_FOLDER, TIME_SESSION

# Khoi tao Flask server 
app = Flask(__name__, template_folder= TEMPLATE_FOLDER)

# Apply flask cors de moi domain khac deu goi duoc
CORS(app)

# config
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = 'dinhchicongf9'
app.permanent_session_lifetime = TIME_SESSION

@app.route('/', methods = ['POST', 'GET'])
@cross_origin(origins='*')
def index():
    return render_template("index.html", content = "Cong pro sieu vip")

@app.route('/admin', methods = ['GET'])
@cross_origin(origins='*')
def admin():
    return "Cong pro la so 1"

@app.route('/user', methods = ['GET'])
@cross_origin(origins='*')
def user():
    if "user" in session:
        name = session['user']
        text = f"Xin chao {name}"
        return text

    text = f"Ban da dang nhap dau ?"
    return text

@app.route('/login', methods = ['GET', 'POST'])
@cross_origin(origins='*')
def login():
    if request.method == "POST":
        email_address = request.form['emailAddress']
        if email_address:
            session.permanent = True
            session['user'] = email_address
            return redirect(url_for("user"))

    return render_template("login.html")

@app.route('/logout', methods = ['GET', 'POST'])
@cross_origin(origins='*')
def logout():
    session.pop("user", None)
    return render_template("login.html")

# @app.route('/add', methods = ['POST', 'GET'])
# @cross_origin(origins='*')
# def add():
#     a = request.form.get("a")
#     b = request.form.get("b")
#     result = int(a) + int(b)
#     return "Ham cong = " + str(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="9999")

