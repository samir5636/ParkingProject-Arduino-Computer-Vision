from database.database import db

class Rapport(db.Model):
    """Model class representing Abonement in the database."""
    id = db.Column(db.Integer, primary_key=True)
    create_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    message = db.Column(db.String(255), nullable=False)
    # Foreign Key to Car
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
