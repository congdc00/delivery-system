
from . import db

class Package(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_package = db.Column(db.Integer, unique=False)
    id_target = db.Column(db.Integer, unique=False )
    time_order = db.Column(db.String(120), unique=False)

    def __init__(self, id_package, id_target, time_order) :

        self.id_package = id_package
        self.id_target = id_target
        self.time_order = time_order


    def __repr__(self):
        return '<Package {}>'.format(self.id_package)  

