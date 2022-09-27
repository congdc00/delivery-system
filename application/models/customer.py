
from . import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False)
    address = db.Column(db.String(120), unique=False)
    phone_num = db.Column(db.String(120), unique=False)
    path_face_id = db.Column(db.String(120), unique=True)

    weight = db.Column(db.Integer, unique=False)
    upper_bound = db.Column(db.Integer, unique=False)
    lower_bound = db.Column(db.Integer, unique=False)


    def __init__(self, name, address, phone_num, path_face_id, weight, upper_bound, lower_bound) :
        self.name = name
        self.address = address
        self.phone_num = phone_num
        self.path_face_id = path_face_id
        self.weight = weight
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound
   

    def __repr__(self):
        return '<Customer {}>'.format(self.name) 