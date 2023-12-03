from models.abonement import Abonement
from models.car import Car
from models.client import Client
from flask import jsonify, request
from database.database import db 
from crud.rapport import create_rapport_by_params_c
from crud.parking import create_rapport_parking_paramrters_c
def get_abonements_c():
    """
    Get a list of all abonements.

    Returns:
        tuple: A tuple containing a JSON response with abonement data and the HTTP status code.
    """
    abonements = Abonement.query.all()
    abonement_data = [{
        'id': abonement.id,
        'create_at': abonement.create_at,
        'sold': abonement.sold,
        'car_id': abonement.car_id
    } for abonement in abonements]
    return jsonify(abonement_data), 200  # 200 OK

def get_abonement_c(id:int):
    """
    Get abonement data by ID.

    Args:
        id (int): The ID of the abonement.

    Returns:
        tuple: A tuple containing a JSON response with abonement data and the HTTP status code.
    """
    try:
        abonement = Abonement.query.get_or_404(id)
        abonement_data = {
            'id': abonement.id,
            'create_at': abonement.create_at,
            'sold': abonement.sold,
            'car_id': abonement.car_id
        }
        return jsonify(abonement_data), 200  # 200 OK
    except:
        return jsonify({'message': f'Abonement not exist with this id {id}'}), 404  # 404 Not Found

def get_abonement_by_matricule_car_c(matricule:str):
    """
    Get abonement data by car matricule.

    Args:
        matricule (str): The matricule of the car.

    Returns:
        tuple: A tuple containing a JSON response with abonement data and the HTTP status code.
    """
    try:
        car = Car.query.filter_by(matricule=matricule).first_or_404()
        abonement = Abonement.query.filter_by(car_id=car.id).first_or_404()
        abonement_data = {
            'id': abonement.id,
            'create_at': abonement.create_at,
            'sold': abonement.sold,
            'car_id': abonement.car_id
        }
        return jsonify(abonement_data), 200  # 200 OK
    except:
        return jsonify({'message': f'Abonement not exist with this car matricule {matricule}'}), 404  # 404 Not Found

def create_abonement_c():
    """
    Create a new abonement.

    Returns:
        tuple: A tuple containing a JSON response with the creation status and the HTTP status code.
    """
    car_id = request.json.get('car_id')
    if Car.car_exists_by_id(car_id):
        sold = request.json.get('sold')
        if not all([sold, car_id]):
            return jsonify({'message': 'Incomplete data provided'}), 400  # 400 Bad Request
        existing_abonemnt = Abonement.query.filter_by(car_id=car_id).first()
        if existing_abonemnt:
            return jsonify({'message': 'Abonement already exists'}), 409  # 409 Conflict
        new_abonement = Abonement(
            sold=sold,
            car_id=car_id
        )
        car=Car.query.filter_by(id=car_id).first()
        db.session.add(new_abonement)
        db.session.commit()
        create_rapport_parking_paramrters_c(False,car_id,False,f"Cretae abonement with id : {new_abonement.id}, for car(matricule={car.matricule},client fullname={Client.query.filter_by(id=car.client_id).first().fullname}))")
        create_rapport_by_params_c(car_id,f"Cretae abonement with id : {new_abonement.id}, for car(matricule={car.matricule},client fullname={Client.query.filter_by(id=car.client_id).first().fullname}))")
        return jsonify({'message': 'Abonement created successfully'}), 201  # 201 Created
    else:
        return jsonify({'message': f'Car not exist with this id {car_id}'}), 404  # 404 Not found
def create_abonement_matricule_c():
    """
    Create a new abonement.

    Returns:
        tuple: A tuple containing a JSON response with the creation status and the HTTP status code.
    """
    sold = request.json.get('sold')
    matricule = request.json.get('matricule')
    if not all([sold, matricule]):
            return jsonify({'message': 'Incomplete data provided'}), 400  # 400 Bad Request
    if Car.car_exists_by_matricule(matricule):
        car_id=Car.query.filter_by(matricule=matricule).first().id
        existing_abonemnt = Abonement.query.filter_by(car_id=car_id).first()
        if existing_abonemnt:
            return jsonify({'message': 'Abonement already exists'}), 409  # 409 Conflict

        new_abonement = Abonement(
            sold=sold,
            car_id=car_id
        )
        car=Car.query.filter_by(id=car_id).first()
        db.session.add(new_abonement)
        db.session.commit()
        create_rapport_parking_paramrters_c(False,car_id,False,f"Cretae abonement with id : {new_abonement.id}, for car(matricule={car.matricule},client fullname={Client.query.filter_by(id=car.client_id).first().fullname}))")
        create_rapport_by_params_c(car_id,f"Cretae abonement with id : {new_abonement.id}, for car(matricule={car.matricule},client fullname={Client.query.filter_by(id=car.client_id).first().fullname}))")
        return jsonify({'message': 'Abonement created successfully'}), 201  # 201 Created
    else:
        return jsonify({'message': f'Car not exist with this matricule {matricule}'}), 404  # 404 Not found

def update_abonement_c(id:int):
    """
    Update abonement information.

    Args:
        id (int): The ID of the abonement to update.

    Returns:
        tuple: A tuple containing a JSON response with the update status and the HTTP status code.
    """
    try:
        abonement = Abonement.query.get_or_404(id)
        last_sold=abonement.sold
        last_car_id=abonement.car_id
        abonement.sold = request.json.get('sold', abonement.sold)
        abonement.car_id = request.json.get('car_id', abonement.car_id)
        db.session.commit()
        car=Car.query.filter_by(id=abonement.car_id).first()
        if request.json.get('sold'):
            create_rapport_parking_paramrters_c(False,abonement.car_id,False,f"Update solde of car from {last_sold} to {request.json.get('sold')}")
            create_rapport_by_params_c(abonement.car_id,f"Update solde from {last_sold} to {request.json.get('sold')}")
        if request.json.get('car_id'):
            create_rapport_parking_paramrters_c(False,abonement.car_id,False,f"Update solde of car(matricule={car.matricule},client fullname={Client.query.filter_by(id=car.client_id).first().fullname}))  from {last_car_id} to {request.json.get('car_id')}")
            create_rapport_by_params_c(abonement.car_id,f"Update id car of car(matricule={car.matricule},client fullname={Client.query.filter_by(id=car.client_id).first().fullname}))  from {last_car_id} to {request.json.get('car_id')}")
        return jsonify({'message': 'Abonement updated successfully'}), 200  # 200 OK
    except:
        return jsonify({'message': f'Abonement not exist with this id {id}'}), 404  # 404 Not Found

def delete_abonement_c(id:int):
    """
    Delete an abonement.

    Args:
        id (int): The ID of the abonement to delete.

    Returns:
        tuple: A tuple containing a JSON response with the deletion status and the HTTP status code.
    """
    try:
        abonement = Abonement.query.get_or_404(id)
        db.session.delete(abonement)
        db.session.commit()
        car=Car.query.filter_by(id=abonement.car_id).first()
        create_rapport_parking_paramrters_c(False,abonement.car_id,False,f"delete abonement of car(matricule={car.matricule},client fullname={Client.query.filter_by(id=car.client_id).first().fullname}))")
        create_rapport_by_params_c(abonement.car_id,f"delete abonement with id : {abonement.id} and car id : {abonement.car_id}")
        return jsonify({'message': 'Abonement deleted successfully'}), 200  # 200 OK
    except:
        return jsonify({'message': f'Abonement not exist with this id {id}'}), 404  # 404 Not Found
