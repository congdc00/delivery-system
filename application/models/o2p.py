# enterprise to user
from . import db

class O2P(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_order = db.Column(db.Integer, unique=False )
    id_product = db.Column(db.Integer, unique=False)
    number = db.Column(db.Integer, unique=False)

    def __init__(self, id_order, id_product, number) :

        self.id_order = id_order
        self.id_product = id_product
        self.number = number

    def __repr__(self):
        return '<O2P {}>'.format(self.id)  

