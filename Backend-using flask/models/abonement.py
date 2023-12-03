from database.database import db

class Abonement(db.Model):
    """Model class representing Abonement in the database."""
    id = db.Column(db.Integer, primary_key=True)
    create_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    sold = db.Column(db.Float)

    # Foreign Key to Car
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)

    @classmethod
    def abonement_exists_by_id(cls, abonement_id):
        """
        Check if an Abonement with the given ID exists.

        Args:
            abonement_id (int): The ID of the Abonement to check.

        Returns:
            bool: True if the Abonement exists, False otherwise.
        """
        return cls.query.filter_by(id=abonement_id).first() is not None
