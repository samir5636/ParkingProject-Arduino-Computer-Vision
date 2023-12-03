from models.client import Client
from models.car import Car
from flask import jsonify, request
from database.database import db 
from crud.parking import create_rapport_parking_paramrters_c
def get_clients_c():
    """
    Get a list of all clients.

    Returns:
        tuple: A tuple containing a JSON response with client data and the HTTP status code.
    """
    clients = Client.query.all()
    client_data = []
    for client in clients:
        client_data.append({
            'id': client.id,
            'fullname': client.fullname,
            'email': client.email,
            'phone_number': client.phone_number,
            'cin': client.cin,
            'age': client.age,
            'create_at': client.create_at
        })
    return jsonify(client_data), 200  # 200 OK

def get_client_by_id_c(id:int):
    """
    Get client data by ID.

    Args:
        id (int): The ID of the client.

    Returns:
        tuple: A tuple containing a JSON response with client data and the HTTP status code.
    """
    try:
        client = Client.query.get(id)
        client_data = {
            'id': client.id,
            'fullname': client.fullname,
            'email': client.email,
            'phone_number': client.phone_number,
            'cin': client.cin,
            'age': client.age,
            'create_at': client.create_at
        }
        return jsonify(client_data), 200  # 200 OK
    except:
        return jsonify({'message': f'Client not exist with this id {id}'}), 404  # 404 Not Found

def create_client_c():
    """
    Create a new client.

    Returns:
        tuple: A tuple containing a JSON response with the creation status and the HTTP status code.
    """
    fullname = request.json.get('fullname')
    email = request.json.get('email')
    phone_number = request.json.get('phone_number')
    cin = request.json.get('cin')
    age = request.json.get('age')

    if not all([fullname, email, phone_number, cin, age]):
        return jsonify({'message': 'Incomplete data provided'}), 400  # 400 Bad Request

    existing_client = Client.query.filter_by(cin=cin).first()
    if existing_client:
        return jsonify({'message': 'Client already exists'}), 409  # 409 Conflict

    new_client = Client(fullname=fullname, email=email, phone_number=phone_number, cin=cin, age=age)
    db.session.add(new_client)
    db.session.commit()
    create_rapport_parking_paramrters_c(new_client.id,False,False,f"Cretae client client(fullname={new_client.fullname},cin={new_client.cin})")
    return jsonify({'message': 'Client created successfully'}), 201  # 201 Created

def update_client_c(id:int):
    """
    Update client information.

    Args:
        id (int): The ID of the client to update.

    Returns:
        tuple: A tuple containing a JSON response with the update status and the HTTP status code.
    """
    try:
        client = Client.query.get(id)
        if request.json.get('fullname'):
            create_rapport_parking_paramrters_c(client.id,False,False,f"Update fullname client(cin={client.cin}) from {client.fullname} to {request.json.get('fullname')}")
        if request.json.get('email'):
            create_rapport_parking_paramrters_c(client.id,False,False,f"Update email client(cin={client.cin}) from {client.email} to {request.json.get('email')}")
        if request.json.get('phone_number'):
            create_rapport_parking_paramrters_c(client.id,False,False,f"Update phone number client(cin={client.cin}) from {client.phone_number} to {request.json.get('phone_number')}")
        if request.json.get('cin'):
            create_rapport_parking_paramrters_c(client.id,False,False,f"Update cin client(fullname={client.fullname}) from {client.cin} to {request.json.get('cin')}")
        if request.json.get('age'):
            create_rapport_parking_paramrters_c(client.id,False,False,f"Update age client(cin={client.cin}) from {client.age} to {request.json.get('age')}")
        client.fullname = request.json.get('fullname', client.fullname)
        client.email = request.json.get('email', client.email)
        client.phone_number = request.json.get('phone_number', client.phone_number)
        client.cin = request.json.get('cin', client.cin)
        client.age = request.json.get('age', client.age)
        db.session.commit()
        return jsonify({'message': 'Client updated successfully'}), 200  # 200 OK
    except:
        return jsonify({'message': f'Client not exist with this id {id}'}), 404  # 404 Not Found

def delete_client_c(id:int):
    """
    Delete a client.

    Args:
        id (int): The ID of the client to delete.

    Returns:
        tuple: A tuple containing a JSON response with the deletion status and the HTTP status code.
    """
    try:
        client = Client.query.get(id)
        db.session.delete(client)
        db.session.commit()
        create_rapport_parking_paramrters_c(client.id,False,False,f"delete client(cin={client.cin},fullname={client.fullname})")
        return jsonify({'message': 'Client deleted successfully'}), 200  # 200 OK
    except:
        return jsonify({'message': f'Client not exist with this id {id}'}), 404  # 404 Not Found

def get_client_cars(id:int):
    """
    Get a list of cars associated with a client.

    Args:
        id (int): The ID of the client.

    Returns:
        tuple: A tuple containing a JSON response with car data and the HTTP status code.
    """
    cars = Car.query.all()
    car_data = [{
        'id': car.id,
        'matricule': car.matricule,
        'is_in_parking': car.is_in_parking,
        'model': car.model,
        'abonement': {'id': car.abonement.id if car.abonement else None}
    } for car in cars if car.client_id==id]
    return jsonify(car_data), 200  # 200 OK
