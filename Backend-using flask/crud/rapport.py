from models.rapport import Rapport
from flask import jsonify, request
from database.database import db 
from models.car import Car

def get_rapports_c():
    """
    Get a list of all rapports.

    Returns:
        tuple: A tuple containing a JSON response with client data and the HTTP status code.
    """
    rapports = Rapport.query.all()
    rapport_data = []
    for rapport in rapports:
        rapport_data.append({
            'id': rapport.id,
            'car_id': rapport.car_id,
            'message': rapport.message,
            'create_at': rapport.create_at
        })
    return jsonify(rapport_data), 200  # 200 OK
def create_rapport_c():
    """
    Create a new rapport.

    Returns:
        tuple: A tuple containing a JSON response with the creation status and the HTTP status code.
    """
    car_id = request.json.get('car_id')
    message = request.json.get('message')

    if not all([car_id, message]):
        return jsonify({'message': 'Incomplete data provided'}), 400  # 400 Bad Request

    existing_car = Car.query.filter_by(id=car_id).first()
    if existing_car:
        new_rapport = Rapport(car_id=car_id, message=message)
        db.session.add(new_rapport)
        db.session.commit()
        return jsonify({'message': 'rapport created successfully'}), 201  # 201 Created
    return jsonify({'message': f'car not exist with id :  {car_id}'}), 404  # 404 Not found

def get_rapports_by_id_car_c(car_id:int):
    """
    Get a list of all rapports by id car.

    Returns:
        tuple: A tuple containing a JSON response with client data and the HTTP status code.
    """
    if Car.car_exists_by_id(car_id):
        rapports = Rapport.query.all()
        rapport_data = []
        for rapport in rapports:
            if rapport.car_id==car_id:
                rapport_data.append({
                    'id': rapport.id,
                    'car_id': rapport.car_id,
                    'message': rapport.message,
                    'create_at': rapport.create_at
                })
        return jsonify(rapport_data), 200  # 200 OK
    return jsonify({'message': f'car not exist with id :  {car_id}'}), 404  # 404 NOT FOUND
def get_rapports_by_matricule_car_c(car_matricule:str):
    car=Car.query.filter_by(matricule=car_matricule).first()
    if car:
        return get_rapports_by_id_car_c(car.id)
    return jsonify({'message': f'car not exist with matricule :  {car_matricule}'}), 404  # 404 NOT FOUND
     

def create_rapport_by_params_c(car_id:int,message:str):
    """
    Create a new rapport.

    Returns:
        tuple: A tuple containing a JSON response with the creation status and the HTTP status code.
    """
    existing_car = Car.query.filter_by(id=car_id).first()
    if existing_car:
        new_rapport = Rapport(car_id=car_id, message=message)
        db.session.add(new_rapport)
        db.session.commit()
        print({'message': 'rapport created successfully'})
    print({'message': f'car not exist with id :  {car_id}'})