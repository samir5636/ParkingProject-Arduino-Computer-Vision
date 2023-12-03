from models.car import Car
from models.abonement import Abonement
from models.client import Client
from flask import jsonify,request
from crud.car import update_car_c
from crud.client import update_client_c
from crud.abonement import update_abonement_c
from database.database import db
def get_information():
    clients=Client.query.all()
    list_info:list=[]
    if clients:
        i:int=0
        for client in clients:
            cars_client=Car.query.filter_by(client_id=client.id).all()
            if cars_client :
                have_cars=1
                for car in cars_client:
                    if car.abonement:
                        abonement=Abonement.query.filter_by(id=car.abonement.id).first()
                        abonement_sold=abonement.sold
                        abonement_create_at=abonement.create_at
                        have_abonement=1
                    else :
                        abonement_sold=0
                        abonement_create_at=client.create_at
                        have_abonement=0
                    i=i+1
                    list_info.append({
                        "id": i,
                        "client_id":client.id,
                        "car_id":car.id,
                        "abonement_id":abonement.id if abonement_sold else "",
                        "fullname":client.fullname,
                        "cin":client.cin,
                        "email":client.email,
                        "phone_number":client.phone_number,
                        "age":client.age,
                        "sold":abonement_sold,
                        "create_at":abonement_create_at,
                        "model":car.model,
                        "matricule":car.matricule,
                        "is_in_parking":car.is_in_parking,
                        "have_abonement":have_abonement,
                        "have_cars":have_cars
                    })
            else:
                i=i+1
                have_cars=0
                have_abonement=0
                list_info.append({
                    "id": i,
                    "client_id":client.id,
                    "car_id":"",
                    "abonement_id":"",
                    "fullname":client.fullname,
                    "cin":client.cin,
                    "email":client.email,
                    "phone_number":client.phone_number,
                    "age":client.age,
                    "sold":0,
                    "create_at":client.create_at,
                    "model":0,
                    "matricule":0,
                    "is_in_parking":0,
                    "have_abonement":have_abonement,
                    "have_cars":have_cars

                })
    return jsonify(list_info),200

def get_information_by_car_matricule(matricule:str):
    client_id=Car.query.filter_by(matricule=matricule).first().id
    client=Client.query.filter_by(id=client_id).first()
    info:dict={
                    "client_id":"",
                    "car_id":"",
                    "abonement_id":"",
                    "fullname":"",
                    "cin":"",
                    "email":"",
                    "phone_number":"",
                    "age":"",
                    "sold":"",
                    "create_at":"",
                    "model":"",
                    "matricule":"",
                    "is_in_parking":"",
                    "have_abonement":"",
                    "have_cars":""
                }
    if client:
        if Car.car_exists_by_matricule(matricule) :
            have_cars=1
            car=Car.query.filter_by(matricule=matricule).first()
            if Abonement.query.filter_by(car_id=car.id):
                abonement=Abonement.query.filter_by(car_id=car.id).first()
                abonement_sold=abonement.sold
                abonement_create_at=abonement.create_at
                have_abonement=1
            else :
                abonement_sold=0
                abonement_create_at=client.create_at
                have_abonement=0
            info={
                    "client_id":client.id,
                    "car_id":car.id,
                    "abonement_id":abonement.id if have_abonement else "",
                    "fullname":client.fullname,
                    "cin":client.cin,
                    "email":client.email,
                    "phone_number":client.phone_number,
                    "age":client.age,
                    "sold":abonement_sold,
                    "create_at":abonement_create_at,
                    "model":car.model,
                    "matricule":car.matricule,
                    "is_in_parking":car.is_in_parking,
                    "have_abonement":have_abonement,
                    "have_cars":have_cars
            }
        else:
            have_cars=0
            have_abonement=0
            info={
                "client_id":client.id,
                "car_id":"",
                "abonement_id":"",
                "fullname":client.fullname,
                "cin":client.cin,
                "email":client.email,
                "phone_number":client.phone_number,
                "age":client.age,
                "sold":0,
                "create_at":client.create_at,
                "model":0,
                "matricule":0,
                "is_in_parking":0,
                "have_abonement":have_abonement,
                "have_cars":have_cars
                }
    return jsonify(info),200        
def update_info(id_client,id_car,id_abonement):
    """
    Update car information.

    Args:
        id (int): The ID of the car to update.

    Returns:
        tuple: A tuple containing a JSON response with the update status and the HTTP status code.
    """
    client=None
    if id_client:
        if Client.client_exists_by_id(id_client):
            response,status=update_client_c(id_client)
    if id_car:
        if Car.car_exists_by_id(id_car) and status!=404:
            response,status=update_car_c(id_car)
    if id_abonement:
        if Abonement.abonement_exists_by_id(id_abonement) and status!=404:
            response,status=update_abonement_c(id_abonement)
    return jsonify({"message":"information updated successufully"}),200

    


