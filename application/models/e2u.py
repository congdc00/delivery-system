
from . import db

class E2U(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_enterprise = db.Column(db.Integer, unique=False )
    id_user = db.Column(db.Integer, unique=False)
    level = db.Column(db.Integer, unique=False)

    def __init__(self, id_enterprise, id_user, level) :

        self.id_enterprise = id_enterprise
        self.id_user = id_user
        self.level = level

    def __repr__(self):
        return '<E2U {}>'.format(self.id_enterprise)  

