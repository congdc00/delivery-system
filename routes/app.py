from crypt import methods
from flask import Flask
from flask import request, redirect, url_for, render_template
from flask_cors import CORS, cross_origin
from application.config import TEMPLATE_FOLDER

# Khoi tao Flask server 
app = Flask(__name__, template_folder= TEMPLATE_FOLDER)

# Apply flask cors de moi domain khac deu goi duoc
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods = ['POST', 'GET'])
@cross_origin(origins='*')
def index():
    return render_template("index.html")

@app.route('/admin', methods = ['GET'])
@cross_origin(origins='*')
def admin():
    return "Cong pro la so 1"

@app.route('/user/<name>', methods = ['GET'])
@cross_origin(origins='*')
def user(name):
    if name == "admin":
        return redirect(url_for("admin"))

    text = f"Xin chao {name}"
    return text

@app.route('/add', methods = ['POST', 'GET'])
@cross_origin(origins='*')
def add():
    a = request.form.get("a")
    b = request.form.get("b")
    result = int(a) + int(b)
    return "Ham cong = " + str(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="9999")

