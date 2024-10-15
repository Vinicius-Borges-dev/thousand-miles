from app import db

class VehicleModel(db.Model):
    __tablename__ = 'vehicles'

    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(50), nullable=False)
    price_per_day = db.Column(db.Float, nullable=False)
    transmission = db.Column(db.String(50), nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    apresentation_photo = db.Column(db.String(255), nullable=False)
    lateral_photo = db.Column(db.String(255), nullable=False)

    def __init__(self, brand, model, category, year, color, price_per_day, transmission, seats, description, apresentation_photo, lateral_photo):
        self.brand = brand
        self.model = model
        self.category = category
        self.year = year
        self.color = color
        self.price_per_day = price_per_day
        self.transmission = transmission
        self.seats = seats
        self.description = description
        self.apresentation_photo = apresentation_photo
        self.lateral_photo = lateral_photo

    def to_dict(self):
        return {
            'id': self.id,
            'brand': self.brand,
            'model': self.model,
            'category': self.category,
            'year': self.year,
            'color': self.color,
            'price_per_day': self.price_per_day,
            'transmission': self.transmission,
            'seats': self.seats,
            'description': self.description,
            'apresentation_photo': self.apresentation_photo,
            'lateral_photo': self.lateral_photo
        }
    
    
    def __repr__(self):
        return f'<Vehicle {self.brand} {self.model} {self.year}>'