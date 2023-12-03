from flask_app import app,render_template,send_from_directory
from database.database import db
from flask import jsonify
from crud.client import (
    get_clients_c, get_client_by_id_c, create_client_c,
    update_client_c, delete_client_c, get_client_cars
)
from crud.car import (
    get_cars_c, get_car_by_id_c, create_car_c, update_car_c,
    delete_car_c, get_car_by_matricule_c, delete_car_by_matricule_c,
    get_car_ticket_by_id_c, get_car_ticket_by_matricule_c,
    get_number_cars_in_parking, get_cars_in_parking, get_number_cars,
    create_car_cin_c
)
from crud.abonement import (
    get_abonements_c, get_abonement_c, create_abonement_c,
    get_abonement_by_matricule_car_c, update_abonement_c, delete_abonement_c,
    create_abonement_matricule_c
)
from crud.information import (
    get_information,get_information_by_car_matricule,update_info
)
from crud.rapport import (
    get_rapports_c,create_rapport_c,get_rapports_by_id_car_c,get_rapports_by_matricule_car_c
    )
from crud.parking import get_rapports_parking_c
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    print(f"Received request for /{filename}")
    return render_template('index.html')



##### CLIENT

@app.route('/clients', methods=['GET'])
def get_clients():
    """Get all clients."""
    return get_clients_c()

@app.route('/clients/<int:id>', methods=['GET'])
def get_client(id: int):
    """Get a client by ID."""
    return get_client_by_id_c(id)

@app.route('/clients', methods=['POST'])
def create_client():
    """Create a new client."""
    return create_client_c()

@app.route('/clients/<int:id>', methods=['PUT'])
def update_client(id: int):
    """Update a client by ID."""
    return update_client_c(id)

@app.route('/clients/<int:id>', methods=['DELETE'])
def delete_client(id: int):
    """Delete a client by ID."""
    return delete_client_c(id)

@app.route('/clients/<int:id>/cars', methods=['GET'])
def get_cars_of_client(id: int):
    """Get cars associated with a client."""
    return get_client_cars(id)

### CARS

@app.route('/cars', methods=['GET'])
def get_cars():
    """Get all cars."""
    return get_cars_c()

@app.route('/cars/<int:id>', methods=['GET'])
def get_car(id: int):
    """Get a car by ID."""
    return get_car_by_id_c(id)

@app.route('/cars', methods=['POST'])
def create_car():
    """Create a new car."""
    return create_car_c()

@app.route('/cars/add', methods=['POST'])
def create_car_usign_client_cin():
    """Create a new car."""
    return create_car_cin_c()

@app.route('/cars/<int:id>', methods=['PUT'])
def update_car(id: int):
    """Update a car by ID."""
    return update_car_c(id)

@app.route('/cars/<int:id>', methods=['DELETE'])
def delete_car(id):
    """Delete a car by ID."""
    return delete_car_c(id)

@app.route('/cars/<string:matricule>', methods=['GET'])
def get_car_by_matricule(matricule):
    """Get a car by matricule."""
    return get_car_by_matricule_c(matricule)

@app.route('/cars/<string:matricule>', methods=['DELETE'])
def delete_car_by_matricule(matricule):
    """Delete a car by matricule."""
    return delete_car_by_matricule_c(matricule)

@app.route('/cars/ticket/<int:id>', methods=['PUT'])
def get_car_ticket(id: int):
    """Get a ticket for a car by ID."""
    return get_car_ticket_by_id_c(id)

@app.route('/cars/ticket/<string:matricule>', methods=['PUT'])
def get_car_ticket_matricule(matricule: str):
    """Get a ticket for a car by matricule."""
    return get_car_ticket_by_matricule_c(matricule)

@app.route('/cars/nbrinparking', methods=['GET'])
def get_car_number_in_parking():
    """Get the number of cars in parking."""
    return get_number_cars_in_parking()

@app.route('/cars/inparking', methods=['GET'])
def get_in_parking_cars():
    """Get cars currently in parking."""
    return get_cars_in_parking()

@app.route('/cars/nbr', methods=['GET'])
def get_car_number():
    """Get the total number of cars."""
    return get_number_cars()

### ABONEMENTS

@app.route('/abonements', methods=['GET'])
def get_abonements():
    """Get all abonements."""
    return get_abonements_c()

@app.route('/abonements/<int:id>', methods=['GET'])
def get_abonement(id):
    """Get an abonement by ID."""
    return get_abonement_c(id)

@app.route('/abonements/cars/<string:matricule>', methods=['GET'])
def get_abonement_by_matricule_car(matricule: str):
    """Get abonement by matricule of the associated car."""
    return get_abonement_by_matricule_car_c(matricule)

@app.route('/abonements', methods=['POST'])
def create_abonement():
    """Create a new abonement."""
    return create_abonement_c()
@app.route('/abonements/add', methods=['POST'])
def create_abonement_matricule():
    """Create a new abonement."""
    return create_abonement_matricule_c()
@app.route('/abonements/<int:id>', methods=['PUT'])
def update_abonement(id: int):
    """Update an abonement by ID."""
    return update_abonement_c(id)

@app.route('/abonements/<int:id>', methods=['DELETE'])
def delete_abonement(id: int):
    """Delete an abonement by ID."""
    return delete_abonement_c(id)
######## INFORMATION
@app.route('/info', methods=['GET'])
def get_info():
    """GET INFORMATION."""
    return get_information()

@app.route('/info/<string:matricule>', methods=['GET'])
def get_info_matricule(matricule:str):
    """GET INFORMATION BY MATRICULE"""
    return get_information_by_car_matricule(matricule)
@app.route('/info/<int:id_client>', methods=['PUT'])
def update_info_client(id_client:int):
    return update_info(id_client,False,False)
@app.route('/info/<int:id_client>/<int:id_car>', methods=['PUT'])
def update_info_client_and_car(id_client:int,id_car:int):
    return update_info(id_client,id_car,False)
@app.route('/info/<int:id_client>/<int:id_car>/<int:id_abonement>', methods=['PUT'])
def update_info_client_and_car_and_abonement(id_client:int,id_car:int,id_abonement:int):
    return update_info(id_client,id_car,id_abonement)
#### Rapports
@app.route('/rapport', methods=['GET'])
def get_rapports():
    """GET INFORMATION."""
    return get_rapports_c()
@app.route('/rapport', methods=['POST'])
def create_rapport():
    """GET INFORMATION."""
    return create_rapport_c()
@app.route('/rapport/<int:car_id>', methods=['GET'])
def get_rapports_by_id_car(car_id:int):
    """GET INFORMATION."""
    return get_rapports_by_id_car_c(car_id)
@app.route('/rapport/<string:car_matricule>', methods=['GET'])
def get_rapports_by_matricule_car(car_matricule:str):
    """GET INFORMATION."""
    return get_rapports_by_matricule_car_c(car_matricule)
@app.route('/parking', methods=['GET'])
def get_rapports_parking():
    """GET INFORMATION."""
    return get_rapports_parking_c()
if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=8000)
    print("Hello Guys")
    

