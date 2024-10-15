from typing import IO

from app.models.VehicleModel import VehicleModel

from app.middlewares.ImageMiddleware import ImageMiddleWare

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
        self.__description = req.form["description"]
        self.__apresentationPhoto = req.files["apresentationPhoto"]
        self.__lateralPhoto = req.files["lateralPhoto"]

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
            
            apresentation_photo_path = apresentation_photo_path.replace("app/", "")
            lateral_photo_path = lateral_photo_path.replace("app/", "")

            newVehicle = self.__VehicleModel(
                brand=self.__brand,
                model=self.__model,
                category=self.__category,
                year=self.__year,
                color=self.__color,
                price_per_day=self.__pricePerDay,
                description=self.__description,
                apresentation_photo=apresentation_photo_path,
                lateral_photo=lateral_photo_path,
            )

            db.session.add(newVehicle)
            db.session.commit()

            return res({"status": "ok"}), 200

        else:

            return res({"status": "error"}), 400

    def index(self, res):
        vehicles = self.__VehicleModel.query.all()
        if vehicles:
            allVehicles = [self.__VehicleModel.to_dict(vehicle) for vehicle in vehicles]
            return res({"vehicles": allVehicles}), 200
        else:
            return res({"status": "error", "message": "Nenhum veículo encontrado"}), 404
