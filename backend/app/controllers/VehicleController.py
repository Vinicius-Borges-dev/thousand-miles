from typing import IO

from app.models.VehicleModel import VehicleModel

from app.middlewares.ImageMiddleware import ImageMiddleWare
from app.middlewares.VehicleMiddleware import VehicleMiddleware

from flask import current_app as app, url_for
import os

from app import db

from werkzeug.utils import secure_filename


class VehicleController:

    __brand: str
    __model: str
    __category: str
    __year: int
    __color: str
    __pricePerDay: float
    __transmission: str
    __seats: int
    __description: str
    __apresentationPhoto: IO
    __lateralPhoto: IO
    __VehicleModel: VehicleModel

    def __init__(self):
        self.__VehicleModel = VehicleModel

    def add_vehicle(self, req, res):

        imageValidator = ImageMiddleWare()

        self.__brand = req.form["brand"]
        self.__model = req.form["model"]
        self.__category = req.form["category"]
        self.__year = int(req.form["year"])
        self.__color = req.form["color"]
        self.__pricePerDay = float(req.form["pricePerDay"].replace(",", "."))
        self.__transmission = req.form["transmission"]
        self.__seats = int(req.form["seats"])
        self.__description = req.form["description"]
        self.__apresentationPhoto = req.files["apresentationPhoto"]
        self.__lateralPhoto = req.files["lateralPhoto"]

        if (
            not self.__brand
            or not self.__model
            or not self.__category
            or not self.__year
            or not self.__color
            or not self.__pricePerDay
            or not self.__transmission
            or not self.__seats
            or not self.__description
            or not self.__apresentationPhoto
            or not self.__lateralPhoto
        ):
            return res({"status": "error", "message": "Preencha todos os campos"}), 422
        else:
            if not VehicleMiddleware().check_vehicle_exists(self.__model, self.__brand):
                if imageValidator.validate_image(
                    self.__apresentationPhoto
                ) and imageValidator.validate_image(self.__lateralPhoto):

                    apresentation_photo_secure_filename = secure_filename(
                        self.__apresentationPhoto.filename
                    )
                    lateral_photo_secure_filename = secure_filename(
                        self.__lateralPhoto.filename
                    )
                    apresentation_photo_path = os.path.join(
                        app.config["UPLOAD_FOLDER"], apresentation_photo_secure_filename
                    )
                    lateral_photo_path = os.path.join(
                        app.config["UPLOAD_FOLDER"], lateral_photo_secure_filename
                    )

                    self.__apresentationPhoto.save(apresentation_photo_path)
                    self.__lateralPhoto.save(lateral_photo_path)

                    apresentation_photo_path = apresentation_photo_path.replace(
                        "app/", ""
                    )
                    lateral_photo_path = lateral_photo_path.replace("app/", "")

                    newVehicle = self.__VehicleModel(
                        brand=self.__brand,
                        model=self.__model,
                        category=self.__category,
                        year=self.__year,
                        color=self.__color,
                        price_per_day=self.__pricePerDay,
                        transmission=self.__transmission,
                        seats=self.__seats,
                        description=self.__description,
                        apresentation_photo=apresentation_photo_path,
                        lateral_photo=lateral_photo_path,
                    )

                    db.session.add(newVehicle)
                    db.session.commit()

                    return (
                        res(
                            {
                                "status": "ok",
                                "message": "Veículo adicionado com sucesso!",
                            }
                        ),
                        200,
                    )
                else:
                    return res({"status": "error", "message": "Imagem inválida"}), 415
            else:
                return res({"status": "error", "message": "Veículo já cadastrado"}), 409

    def index(self, res):
        vehicles = self.__VehicleModel.query.all()
        if vehicles:
            allVehicles = [self.__VehicleModel.to_dict(vehicle) for vehicle in vehicles]
            return res({"vehicles": allVehicles}), 200
        else:
            return res({"status": "error", "message": "Nenhum veículo encontrado"}), 404

    def update_vehicles(req, res):

        self.__brand = req.form["brand"]
        self.__model = req.form["model"]
        self.__category = req.form["category"]
        self.__year = int(req.form["year"])
        self.__color = req.form["color"]
        self.__pricePerDay = float(req.form["pricePerDay"].replace(",", "."))
        self.__transmission = req.form["transmission"]
        self.__seats = int(req.form["seats"])
        self.__description = req.form["description"]
        self.__apresentationPhoto = req.files["apresentationPhoto"]
        self.__lateralPhoto = req.files["lateralPhoto"]

        if (
            not self.__brand
            or not self.__model
            or not self.__category
            or not self.__year
            or not self.__color
            or not self.__pricePerDay
            or not self.__transmission
            or not self.__seats
            or not self.__description
            or not self.__apresentationPhoto
            or not self.__lateralPhoto
        ):
            return res({"status": "error", "message": "Preencha todos os campos"}), 422
        else:
            vehicle = VehicleModel.query.filter_by(id=req.form["id"]).first()

            if vehicle:
                vehicle.brand = self.__brand
                vehicle.model = self.__model
                vehicle.category = self.__category
                vehicle.year = self.__year
                vehicle.color = self.__color
                vehicle.price_per_day = self.__pricePerDay
                vehicle.transmission = self.__transmission
                vehicle.seats = self.__seats
                vehicle.description = self.__description

                imageValidator = ImageMiddleWare()

                if imageValidator.validate_image(self.__apresentationPhoto):
                    apresentation_photo_secure_filename = secure_filename(
                        self.__apresentationPhoto.filename
                    )
                    apresentation_photo_path = os.path.join(
                        app.config["UPLOAD_FOLDER"], apresentation_photo_secure_filename
                    )
                    self.__apresentationPhoto.save(apresentation_photo_path)
                    apresentation_photo_path = apresentation_photo_path.replace(
                        "app/", ""
                    )

                    if vehicle.apresentation_photo != apresentation_photo_path:
                        old_apresentation_photo_path = os.path.join(
                            "app", vehicle.apresentation_photo
                        )
                        if os.path.exists(old_apresentation_photo_path):
                            os.remove(old_apresentation_photo_path)

                    vehicle.apresentation_photo = apresentation_photo_path

                if imageValidator.validate_image(self.__lateralPhoto):
                    lateral_photo_secure_filename = secure_filename(
                        self.__lateralPhoto.filename
                    )
                    lateral_photo_path = os.path.join(
                        app.config["UPLOAD_FOLDER"], lateral_photo_secure_filename
                    )
                    self.__lateralPhoto.save(lateral_photo_path)
                    lateral_photo_path = lateral_photo_path.replace("app/", "")

                    if vehicle.lateral_photo != lateral_photo_path:
                        old_lateral_photo_path = os.path.join(
                            "app", vehicle.lateral_photo
                        )
                        if os.path.exists(old_lateral_photo_path):
                            os.remove(old_lateral_photo_path)

                    vehicle.lateral_photo = lateral_photo_path

                db.session.commit()

                return (
                    res({"status": "ok", "message": "Veículo atualizado com sucesso"}),
                    200,
                )
            else:
                return (
                    res({"status": "error", "message": "Veículo não encontrado"}),
                    404,
                )

    def get_vehicle_by_id(self, id, res):
        vehicle = self.__VehicleModel.query.filter_by(id=int(id)).first()
        if vehicle:
            vehicle_data = self.__VehicleModel.to_dict(vehicle)
            return (
                res(
                    {
                        "status": "ok",
                        "message": "Veículo encontrado",
                        "vehicle": vehicle_data,
                    }
                ),
                200,
            )
        else:
            return res({"status": "error", "message": "Veículo não encontrado!"}), 404

    def delete_vehicle(self, req, res):
        vehicle = self.__VehicleModel.query.filter_by(id=req.form["id"]).first()
        if vehicle:
            db.session.delete(vehicle)
            db.session.commit()
            return res({"status": "ok", "message": "Veículo deletado com sucesso"}), 200
        else:
            return res({"status": "error", "message": "Veículo não encontrado"}), 404
