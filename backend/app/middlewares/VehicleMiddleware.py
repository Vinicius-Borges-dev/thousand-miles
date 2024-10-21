from app.models.VehicleModel import VehicleModel


class VehicleMiddleware:
    def check_vehicle_exists(self, vehicle_model, vehicle_brand):
        vehicle = VehicleModel.query.filter_by(
            model=vehicle_model, brand=vehicle_brand
        ).first()
        if vehicle:
            return True
        return False
