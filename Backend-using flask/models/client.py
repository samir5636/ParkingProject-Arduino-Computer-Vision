from database.database import db

class Client(db.Model):
    """Model class representing Client in the database."""
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=False, nullable=False)
    phone_number = db.Column(db.String(255), nullable=False)
    cin = db.Column(db.String(255), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    create_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    # One-to-Many relationship with Car
    cars = db.relationship('Car', backref='client', lazy=True)

    @classmethod
    def client_exists_by_id(cls, client_id):
        """
        Check if a Client with the given ID exists.

        Args:
            client_id (int): The ID of the Client to check.

        Returns:
            bool: True if the Client exists, False otherwise.
        """
        return cls.query.filter_by(id=client_id).first() is not None

    @classmethod
    def client_exists_by_cin(cls, cin):
        """
        Check if a Client with the given ID exists.

        Args:
            client_id (int): The ID of the Client to check.

        Returns:
            bool: True if the Client exists, False otherwise.
        """
        return cls.query.filter_by(cin=cin).first() is not None
    
    def __str__(self):
        """
        Return a human-readable string representation of the Client.

        Returns:
            str: String representation of the Client.
        """
        return f"Client(id={self.id}, fullname='{self.fullname}', email='{self.email}', phone_number='{self.phone_number}', cin='{self.cin}', age={self.age}, create_at={self.create_at})"
