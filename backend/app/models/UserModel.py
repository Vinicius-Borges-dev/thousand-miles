from app import db
import enum
from sqlalchemy import Enum

class EnumRole(enum.Enum):
    defaultUser = "user"
    employee = "employee"

class UserModel(db.Model):
    
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    rg = db.Column(db.String(9), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    access_level = db.Column(Enum(EnumRole), nullable=False)

    def __init__(self, name, email, password, cpf, rg, birth_date, access_level):
        self.name = name
        self.email = email
        self.password = password
        self.cpf = cpf
        self.rg = rg
        self.birth_date = birth_date
        self.access_level = access_level

    def __repr__(self):
        return f'<User {self.name} {self.email}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'cpf': self.cpf,
            'rg': self.rg,
            'birth_date': self.birth_date,
            'access_level': self.access_level.value
        }