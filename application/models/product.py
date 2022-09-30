
from . import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique = False)
    id_product = db.Column(db.Integer, unique=False)
    weight = db.Column(db.Integer, unique=False)
    id_deport = db.Column(db.Integer, unique=False)

    id_root = db.Column(db.Integer, unique=False) # nguoi tao ra product
    is_user = db.Column(db.Boolean, unique=False)
    
    def __init__(self,name, id_product,weight, id_deport, id_root, is_user) :

        self.name = name
        self.id_product = id_product
        self.weight = weight
        self.id_deport = id_deport
        self.id_root =id_root
        self.is_user = is_user


    def __repr__(self):
        return '<Product {}>'.format(self.name) 