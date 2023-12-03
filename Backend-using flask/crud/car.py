from models.client import Client
from models.car import Car
from flask import jsonify, request
from database.database import db 
from crud.rapport import create_rapport_by_params_c
from crud.parking import create_rapport_parking_paramrters_c
ticket=12
def get_cars_c():
    """
    Get a list of all cars.

    Returns:
        tuple: A tuple containing a JSON response with car data and the HTTP status code.
    """
    cars = Car.query.all()
    car_data = [{
        'id': car.id,
        'matricule': car.matricule,
        'is_in_parking': car.is_in_parking,
        'model': car.model,
        'client_id': car.client_id,
        'abonement': {'id': car.abonement.id if car.abonement else None}
    } for car in cars]
    return jsonify(car_data), 200  # 200 OK 

def create_car_c():
    """
    Create a new car.

    Returns:
        tuple: A tuple containing a JSON response with the creation status and the HTTP status code.
    """
    client_id = request.json.get('client_id')
    if Client.client_exists_by_id(client_id):
        matricule = request.json.get('matricule')
        model = request.json.get('model')
        if not all([matricule, model, client_id]):
            return jsonify({'message': 'Incomplete data provided'}), 400  # 400 Bad Request

        existing_car = Car.query.filter_by(matricule=matricule).first()
        if existing_car:
            return jsonify({'message': 'Car already exists'}), 409  # 409 Conflict
        client = Client.query.filter_by(id=client_id).first()
        new_car = Car(matricule=request.json.get('matricule'),is_in_parking=request.json.get('is_in_parking'),model=request.json.get('model'),client_id=request.json.get('client_id'))
        db.session.add(new_car)
        db.session.commit()
        create_rapport_by_params_c(new_car.id,f"Car with id : {new_car.id} and client id : {client_id} created successfully")
        create_rapport_parking_paramrters_c(client.id,False,False,f"Add new car with matricule {new_car.matricule} to client : fullname = {client.fullname},cin={client.cin},id={client.id}")
        return jsonify({'message': 'Car created successfully'}), 201  # 201 Created
    else:
         return jsonify({'message': f'Client not exist with this id {request.json.get("client_id")}'}), 404  # 404 Not Found

def create_car_cin_c():
    """
    Create a new car.

    Returns:
        tuple: A tuple containing a JSON response with the creation status and the HTTP status code.
    """
    cin = request.json.get('cin')
    if Client.client_exists_by_cin(cin):
        matricule = request.json.get('matricule')
        model = request.json.get('model')
        if not all([matricule, model, cin]):
            return jsonify({'message': 'Incomplete data provided'}), 400  # 400 Bad Request

        existing_car = Car.query.filter_by(matricule=matricule).first()
        if existing_car:
            return jsonify({'message': 'Car already exists'}), 409  # 409 Conflict
        client=Client.query.filter_by(cin=cin).first()
        new_car = Car(matricule=request.json.get('matricule'),is_in_parking=request.json.get('is_in_parking'),model=request.json.get('model'),client_id=client.id)
        db.session.add(new_car)
        db.session.commit()
        create_rapport_by_params_c(new_car.id,f"Car with id : {new_car.id} and client id : {client.id} created successfully")
        create_rapport_parking_paramrters_c(client.id,False,False,f"Add new car with matricule {new_car.matricule} to client : fullname = {client.fullname},cin={client.cin},id={client.id}")
        return jsonify({'message': 'Car created successfully'}), 201  # 201 Created
    else:
         return jsonify({'message': f'Client not exist with this cin {cin}'}), 404  # 404 Not Found

def update_car_c(id:int):
    """
    Update car information.

    Args:
        id (int): The ID of the car to update.

    Returns:
        tuple: A tuple containing a JSON response with the update status and the HTTP status code.
    """
    try:
        car = Car.query.get(id)
        if request.json.get('matricule'):
            create_rapport_parking_paramrters_c(False,car.id,False,f"update matricule car(matricule={car.matricule}) of client {Client.query.filter_by(id=car.client_id).first().fullname} from {car.matricule} to {request.json.get('matricule')}")
            create_rapport_by_params_c(car.id,f"update matricule car(matricule={car.matricule}) of client {Client.query.filter_by(id=car.client_id).first().fullname} from {car.matricule} to {request.json.get('matricule')}")
        if request.json.get('is_in_parking'):
            create_rapport_parking_paramrters_c(False,car.id,False,f"update is_in_parking car(matricule={car.matricule}) of client {Client.query.filter_by(id=car.client_id).first().fullname} from {car.is_in_parking} to {request.json.get('is_in_parking')}")
            create_rapport_by_params_c(car.id,f"update is_in_parking car of client {Client.query.filter_by(id=car.client_id).first().fullname} from {car.is_in_parking} to {request.json.get('is_in_parking')}")
        if request.json.get('model'):
            create_rapport_parking_paramrters_c(False,car.id,False,f"update model car(matricule={car.matricule}) of client {Client.query.filter_by(id=car.client_id).first().fullname} from {car.model} to {request.json.get('model')}")
            create_rapport_by_params_c(car.id,f"update model car(matricule={car.matricule}) of client {Client.query.filter_by(id=car.client_id).first().fullname} from {car.model} to {request.json.get('model')}")
        if request.json.get('client_id'):
            create_rapport_by_params_c(car.id,f"update client id car(matricule={car.matricule}) of client {Client.query.filter_by(id=car.client_id).first().fullname} from {car.client_id} to {request.json.get('client_id')}")
            create_rapport_parking_paramrters_c(False,car.id,False,f"update client id car(matricule={car.matricule}) of client {Client.query.filter_by(id=car.client_id).first().fullname} from from {car.client_id} to {request.json.get('client_id')}")
        car.matricule = request.json.get('matricule', car.matricule)
        car.is_in_parking = request.json.get('is_in_parking', car.is_in_parking)
        car.model = request.json.get('model', car.model)
        car.client_id = request.json.get('client_id', car.client_id)
        db.session.commit()
        return jsonify({'message': 'Car updated successfully'}), 200  # 200 OK
    except:
        return jsonify({'message': f'Car not exist with this id {id}'}), 404  # 404 Not Found

def delete_car_c(id:int):
    """
    Delete a car.

    Args:
        id (int): The ID of the car to delete.

    Returns:
        tuple: A tuple containing a JSON response with the deletion status and the HTTP status code.
    """
    try:
        car = Car.query.get(id)
        db.session.delete(car)
        db.session.commit()
        create_rapport_parking_paramrters_c(False,car.id,False,f"delte car(matricule={car.matricule}) of client {Client.query.filter_by(id=car.client_id).first().fullname}")
        create_rapport_by_params_c(car.id,f"delete car(matricule={car.matricule}) with id  {car.id} of client {Client.query.filter_by(id=car.client_id).first().fullname}")
        return jsonify({'message': 'Car deleted successfully'}), 200  # 200 OK
    except:
        return jsonify({'message': f'Car not exist with this id {id}'}), 404  # 404 Not Found    

def get_car_by_id_c(id:int):
    """
    Get car data by ID.

    Args:
        id (int): The ID of the car.

    Returns:
        tuple: A tuple containing a JSON response with car data and the HTTP status code.
    """
    try:
        car = Car.query.get(id)
        car_data = {
            'id': car.id,
            'matricule': car.matricule,
            'is_in_parking': car.is_in_parking,
            'model': car.model,
            'client_id': car.client_id,
            'abonement': {'id': car.abonement.id if car.abonement else None}
        }
        return jsonify(car_data), 200  # 200 OK
    except:
        return jsonify({'message': f'Car not exist with this id {id}'}), 404  # 404 Not Found

def delete_car_by_matricule_c(matricule: str):
    """
    Delete a car by matricule.

    Args:
        matricule (str): The matricule of the car to delete.

    Returns:
        tuple: A tuple containing a JSON response with the deletion status and the HTTP status code.
    """
    try:
        car = Car.query.filter_by(matricule=matricule).first_or_404()
        db.session.delete(car)
        db.session.commit()
        create_rapport_parking_paramrters_c(False,car.id,False,f"delte car(matricule={car.matricule}) of client {Client.query.filter_by(id=car.client_id).first().fullname}")
        create_rapport_by_params_c(car.id,f"delete car(matricule={car.matricule}) of client {Client.query.filter_by(id=car.client_id).first().fullname}")
        return jsonify({'message': 'Car deleted successfully'}), 200  # 200 OK
    except:
        return jsonify({'message': f'Car not exist with this matricule {matricule}'}), 404  # 404 Not Found

def get_car_by_matricule_c(matricule: str):
    """
    Get car data by matricule.

    Args:
        matricule (str): The matricule of the car.

    Returns:
        tuple: A tuple containing a JSON response with car data and the HTTP status code.
    """
    try:
        car = Car.query.filter_by(matricule=matricule).first_or_404()
        car_data = {
            'id': car.id,
            'matricule': car.matricule,
            'is_in_parking': car.is_in_parking,
            'model': car.model,
            'client_id': car.client_id,
            'abonement': {'id': car.abonement.id if car.abonement else None}
        }
        return jsonify(car_data), 200  # 200 OK
    except:
        return jsonify({'message': f'Car not exist with this matricule {matricule}'}), 404  # 404 Not Found

def get_car_ticket_by_id_c(id:int):
    """
    Process a car ticket by ID.

    Args:
        id (int): The ID of the car.

    Returns:
        tuple: A tuple containing a JSON response with the ticket processing status and the HTTP status code.
    """
    try:
        global ticket
        car = Car.query.get(id)
        if not car.is_in_parking:
            car.is_in_parking = True
            car.abonement.sold -= ticket
            db.session.commit()
            return jsonify({'message': 'Car ticket successfully processed'}), 200  # 200 OK
    except:
        return jsonify({'message': f'Car not exist with this id {id}'}), 404  # 404 Not Found

def get_car_ticket_by_matricule_c(matricule:str):
    """
    Process a car ticket by matricule.

    Args:
        matricule (str): The matricule of the car.

    Returns:
        tuple: A tuple containing a JSON response with the ticket processing status and the HTTP status code.
    """
    try:
        
        car = Car.query.filter_by(matricule=matricule).first_or_404()
        if not car.is_in_parking:
            car.is_in_parking = True
            car.abonement.sold -= ticket
            db.session.commit()
            return jsonify({'message': 'Car ticket successfully processed'}), 200  # 200 OK
    except:
        return jsonify({'message': f'Car not exist with this matricule {matricule}'}), 404  # 404 Not Found

def get_number_cars_in_parking():
    """
    Get the number of cars in the parking.

    Returns:
        tuple: A tuple containing a JSON response with the number of cars and the HTTP status code.
    """
    number=0
    cars = Car.query.all()
    for car in cars:
        if car.is_in_parking:
            number += 1
    return jsonify({"number": number}), 200  # 200 OK 

def get_cars_in_parking():
    """
    Get a list of cars currently in the parking.

    Returns:
        tuple: A tuple containing a JSON response with car data and the HTTP status code.
    """
    cars = Car.query.all()
    car_data = [{
        'id': car.id,
        'matricule': car.matricule,
        'is_in_parking': car.is_in_parking,
        'model': car.model,
        'client_id': car.client_id,
        'abonement': {'id': car.abonement.id if car.abonement else None}
    } for car in cars if car.is_in_parking]
    return jsonify(car_data), 200  # 200 OK 

def get_number_cars():
    """
    Get the total number of cars.

    Returns:
        tuple: A tuple containing a JSON response with the number of cars and the HTTP status code.
    """
    cars = Car.query.all()
    return jsonify({"number": len(cars)}), 200  # 200 OK
