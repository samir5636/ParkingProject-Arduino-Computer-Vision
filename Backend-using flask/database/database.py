from flask_app import app
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:samir5636123@localhost:3306/parking'
db = SQLAlchemy(app)