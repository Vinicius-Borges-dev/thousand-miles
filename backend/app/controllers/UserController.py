from app.models.UserModel import UserModel, EnumRole
from datetime import datetime, date, timedelta
from app import db
from app.middlewares.Usermiddleware import UserMiddleware
import bcrypt
import jwt
from flask import current_app as app


class UserController:

    __name: str
    __email: str
    __password: str
    __cpf: str
    __rg: str
    __birth_date: str
    __access_level: str

    def __init__(self):
        self.__user_middleware = UserMiddleware()
        self.__user_model = UserModel

    def create_user(self, req, res):
        self.__name = req.form["signup_name"]
        self.__email = req.form["signup_email"]
        self.__birth_date = datetime.strptime(req.form["signup_birthdate"], '%Y-%m-%d').date()
        self.__rg = req.form["signup_rg"]
        self.__cpf = req.form["signup_cpf"]
        self.__password = req.form["signup_password"]
        
        print(self.__cpf)
        print(self.__rg)

        if (
            not self.__name
            or not self.__email
            or not self.__password
            or not self.__cpf
            or not self.__rg
            or not self.__birth_date
        ):
            return (
                res({"status": "error", "message": "Campos não foram preenchidos!"}),
                422,
            )

        if self.__user_middleware.check_user_already_exists(self.__cpf, self.__rg):
            return (
                res(
                    {
                        "status": "error",
                        "message": "Já existe um usuário com essa crendênciais!",
                    }
                ),
                409
            )

        self.__password = self.hash_password(self.__password)

        newUser = self.__user_model(
            name=self.__name,
            email=self.__email,
            password=self.__password,
            cpf=self.__cpf,
            rg=self.__rg,
            birth_date=self.__birth_date,
            access_level=EnumRole.defaultUser,
        )
        db.session.add(newUser)
        db.session.commit()

        return res({"status": "ok", "message": "Cadastro concluido com sucesso!"}), 201

    @staticmethod
    def hash_password(password):
        salt = bcrypt.gensalt()

        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)

        return hashed_password

    def login(self, req, res):
        self.__email = req.form["login_email"]
        self.__password = req.form["login_password"]

        user = self.__user_model.query.filter_by(email=self.__email).first()
        if not user:
            return (res({"status": "error", "message": "Usupario não encotrado!"}), 404)

        user_dict = self.__user_model.to_dict(user)
        if not self.__user_middleware.verify_passwords_match(
            user_dict['password'], self.__password
        ):
            return (res({"status": "erro", "message": "Senhas não conferem!"}), 400)

        token_data = {
            "id": user_dict['id'],
            "name": user_dict['name'],
            "access_level": user_dict['access_level'],
            "exp": datetime.utcnow() + timedelta(hours=2),
        }

        token = jwt.encode(token_data, app.config["SECRET_KEY"])

        return (
            res({"status": "ok", "message": "Login realizado!", "token": token}),
            200,
        )
