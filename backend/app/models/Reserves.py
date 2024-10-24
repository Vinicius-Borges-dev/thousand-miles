from app import db


class Reserves(db.Model):

    __tablename__ = "reserves"

    id = db.Column(db.String(), primary_key=True)
    
