"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/people', methods=['GET'])
def get_people():
    name = request.json.get("name", None)
    gender = request.json.get("gender", None)
    hair_color = request.json.get("hair_color", None)
    eye_color = request.json.get("eye_color", None)

    if name is None:
        return jsonify({"msg": "Name is required"}), 400
    if gender is None:
        return jsonify({"msg": "Gender is required"}), 400
    if hair_color is None:
        return jsonify({"msg": "Hair Color is required"}), 400
    if eye_color is None:
        return jsonify({"msg": "Eye color is required"}), 400

    people = people.query.filter_by(name=name, gender=gender,hair_color=hair_color,eye_color=eye_color).first()

    if people:
        # the user was not found on the database
        return jsonify({"msg": "character was already registered"}), 401
    else:
        # crea usuario nuevo
        # crea registro nuevo en BBDD de
        people = people(name=name, gender=gender, hair_color=hair_color,eye_color=eye_color)
        db.session.add(people)
        db.session.commit()


    response_body = {
        "msg": "Hello, this is your GET /people response "
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
