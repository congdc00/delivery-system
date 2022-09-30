
from . import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False)
    address = db.Column(db.String(120), unique=False)
    phone_num = db.Column(db.String(120), unique=False)
    path_face_id = db.Column(db.String(120), unique=False)

    weight = db.Column(db.Integer, unique=False)
    upper_bound = db.Column(db.Integer, unique=False)
    lower_bound = db.Column(db.Integer, unique=False)

    id_root = db.Column(db.Integer, unique=False) # nguoi tao ra product
    is_user = db.Column(db.Boolean, unique=False)


    def __init__(self, name, address, phone_num, path_face_id, weight, upper_bound, lower_bound, id_root, is_user) :
        self.name = name
        self.address = address
        self.phone_num = phone_num
        self.path_face_id = path_face_id
        self.weight = weight
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound

        self.id_root = id_root
        self.is_user = is_user
   

    def __repr__(self):
        return '<Customer {}>'.format(self.name) 