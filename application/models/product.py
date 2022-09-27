
from . import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_product = db.Column(db.Integer, unique=False)
    weight = db.Column(db.Integer, unique=False)
    number = db.Column(db.Integer, unique=False )
    id_deport = db.Column(db.Integer, unique=False)
    
    def __init__(self, id_product,weight, number, id_deport) :

        self.id_product = id_product
        self.weight = weight
        self.number = number
        self.id_deport = id_deport


    def __repr__(self):
        return '<Product {}>'.format(self.id_product) 