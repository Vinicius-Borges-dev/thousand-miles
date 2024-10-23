from app import db
from app.config import Database
from app.models.UserModel import EnumRole, UserModel
import bcrypt

class UserMiddleware:
    __connection: Database
    
    def __init__(self):
        self.__connection = db
        self.__model = UserModel()
    
    def check_employee_permission(self, role):
        return role == EnumRole.employee
    
    def check_user_already_exists(self, cpf, rg):
        user = self.__model.query.filter_by(cpf=cpf, rg=rg)
        if user:
            return True
        else:
            return False
    
    @staticmethod
    def verify_passwords_match(hashed_password, password_set):
        return bcrypt.checkpw(password_set.encode('utf-8'), hashed_password)