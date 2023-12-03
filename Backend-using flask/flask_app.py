# from flask import Flask,render_template,send_from_directory
# from flask_cors import CORS


# app = Flask(__name__, static_folder='static', template_folder='templates')
# # Enable CORS for all routes
# CORS(app)
from flask import Flask, render_template, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

# Your routes and other configurations go here
