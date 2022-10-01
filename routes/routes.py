
from flask import session
from . import app
from application.controller.index import index_get





@app.route('/', methods = ['POST', 'GET'])
def index():
    return index_get(session)


# @app.route('/add', methods = ['POST', 'GET'])
# @cross_origin(origins='*')
# def add():
#     a = request.form.get("a")
#     b = request.form.get("b")
#     result = int(a) + int(b)
#     return "Ham cong = " + str(result)
    


