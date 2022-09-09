from crypt import methods
from flask import Flask, request
from flask_cors import CORS, cross_origin

# khoi tao flask server
app = Flask(__name__)

#apply flask cors
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#server
@app.route('/add', methods = ["POST", "GET"])
@cross_origin(origins='*')
def add_number():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return "ket qua la" + str(a+b)

@app.route('/minus', methods = ["POST"])
@cross_origin(origins='*')
def minus_number():
    a = request.form.get("a")
    return a.upper()

#start server
if __name__ == "__main__":
    app.run(host = '0.0.0.0', port= '9999')