from models.parking import Parking
from flask import jsonify, request
from database.database import db 
from models.car import Car
from models.client import Client
from models.abonement import Abonement


def get_rapports_parking_c():
    """
    Get a list of all rapports.

    Returns:
        tuple: A tuple containing a JSON response with client data and the HTTP status code.
    """
    rapports = Parking.query.all()
    rapport_data = []
    for rapport in rapports:
        rapport_data.append({
            'id': rapport.id,
            'message': rapport.message,
            'create_at': rapport.create_at
        })
    return jsonify(rapport_data), 200  # 200 OK
def create_rapport_parking_paramrters_c(client_id,car_id,abonement_id,message):
    """
    Create a new rapport.

    Returns:
        tuple: A tuple containing a JSON response with the creation status and the HTTP status code.
    """
    new_rapport=False
    if client_id:
        existing_client=Client.query.filter_by(id=client_id).first()
        if existing_client:
            new_rapport = Parking(message=message)
    elif car_id:
        existing_car = Car.query.filter_by(id=car_id).first()
        if existing_car:
            new_rapport = Parking(message=message)
    elif abonement_id:
        existing_abonement = Abonement.query.filter_by(id=abonement_id).first()
        if existing_abonement:
            new_rapport = Parking(message=message)
    if new_rapport:
        db.session.add(new_rapport)
        db.session.commit()
