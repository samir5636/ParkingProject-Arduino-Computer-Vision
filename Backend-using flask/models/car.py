from database.database import db

class Car(db.Model):
    """Model class representing Car in the database."""
    id = db.Column(db.Integer, primary_key=True)
    matricule = db.Column(db.String(255), nullable=False)
    is_in_parking = db.Column(db.Boolean, default=False)  # True: 1, False: 0
    model = db.Column(db.String(255))
    
    # Foreign Key to Client
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)

    # One-to-One relationship with Abonement
    abonement = db.relationship('Abonement', backref='car', uselist=False, cascade='all, delete-orphan', lazy=True)
    @classmethod
    def car_exists_by_matricule(cls, matricul):
        """
        Check if a Client with the given ID exists.

        Args:
            client_id (int): The ID of the Client to check.

        Returns:
            bool: True if the Client exists, False otherwise.
        """
        return cls.query.filter_by(matricule=matricul).first() is not None
    @classmethod
    def car_exists_by_id(cls, id):
        """
        Check if a Client with the given ID exists.

        Args:
            client_id (int): The ID of the Client to check.

        Returns:
            bool: True if the Client exists, False otherwise.
        """
        return cls.query.filter_by(id=id).first() is not None
    def __str__(self):
        """
        Return a human-readable string representation of the Car.

        Returns:
            str: String representation of the Car.
        """
        return f"Car(id={self.id}, matricule='{self.matricule}', is_in_parking={self.is_in_parking}, model='{self.model}', client_id={self.client_id})"

