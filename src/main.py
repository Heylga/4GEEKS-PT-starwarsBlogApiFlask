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


people = {
  "message": "ok",
  "total_records": 82,
  "total_pages": 9,
  "previous": None,
  "next": "https://www.swapi.tech/api/people?page=2&limit=10",
  "results": [
    {
      "uid": "1",
      "name": "Luke Skywalker",
      "url": "https://www.swapi.tech/api/people/1"
    },
    {
      "uid": "2",
      "name": "C-3PO",
      "url": "https://www.swapi.tech/api/people/2"
    },
    {
      "uid": "3",
      "name": "R2-D2",
      "url": "https://www.swapi.tech/api/people/3"
    },
    {
      "uid": "4",
      "name": "Darth Vader",
      "url": "https://www.swapi.tech/api/people/4"
    },
    {
      "uid": "5",
      "name": "Leia Organa",
      "url": "https://www.swapi.tech/api/people/5"
    },
    {
      "uid": "6",
      "name": "Owen Lars",
      "url": "https://www.swapi.tech/api/people/6"
    },
    {
      "uid": "7",
      "name": "Beru Whitesun lars",
      "url": "https://www.swapi.tech/api/people/7"
    },
    {
      "uid": "8",
      "name": "R5-D4",
      "url": "https://www.swapi.tech/api/people/8"
    },
    {
      "uid": "9",
      "name": "Biggs Darklighter",
      "url": "https://www.swapi.tech/api/people/9"
    },
    {
      "uid": "10",
      "name": "Obi-Wan Kenobi",
      "url": "https://www.swapi.tech/api/people/10"
    }
  ]
}

planets = {
  "message": "ok",
  "total_records": 60,
  "total_pages": 6,
  "previous": None,
  "next": "https://www.swapi.tech/api/planets?page=2&limit=10",
  "results": [
    {
      "uid": "1",
      "name": "Tatooine",
      "url": "https://www.swapi.tech/api/planets/1"
    },
    {
      "uid": "2",
      "name": "Alderaan",
      "url": "https://www.swapi.tech/api/planets/2"
    },
    {
      "uid": "3",
      "name": "Yavin IV",
      "url": "https://www.swapi.tech/api/planets/3"
    },
    {
      "uid": "4",
      "name": "Hoth",
      "url": "https://www.swapi.tech/api/planets/4"
    },
    {
      "uid": "5",
      "name": "Dagobah",
      "url": "https://www.swapi.tech/api/planets/5"
    },
    {
      "uid": "6",
      "name": "Bespin",
      "url": "https://www.swapi.tech/api/planets/6"
    },
    {
      "uid": "7",
      "name": "Endor",
      "url": "https://www.swapi.tech/api/planets/7"
    },
    {
      "uid": "8",
      "name": "Naboo",
      "url": "https://www.swapi.tech/api/planets/8"
    },
    {
      "uid": "9",
      "name": "Coruscant",
      "url": "https://www.swapi.tech/api/planets/9"
    },
    {
      "uid": "10",
      "name": "Kamino",
      "url": "https://www.swapi.tech/api/planets/10"
    }
  ]
}

starships = {
  "message": "ok",
  "total_records": 36,
  "total_pages": 4,
  "previous": None,
  "next": "https://www.swapi.tech/api/starships?page=2&limit=10",
  "results": [
    {
      "uid": "2",
      "name": "CR90 corvette",
      "url": "https://www.swapi.tech/api/starships/2"
    },
    {
      "uid": "3",
      "name": "Star Destroyer",
      "url": "https://www.swapi.tech/api/starships/3"
    },
    {
      "uid": "5",
      "name": "Sentinel-class landing craft",
      "url": "https://www.swapi.tech/api/starships/5"
    },
    {
      "uid": "9",
      "name": "Death Star",
      "url": "https://www.swapi.tech/api/starships/9"
    },
    {
      "uid": "11",
      "name": "Y-wing",
      "url": "https://www.swapi.tech/api/starships/11"
    },
    {
      "uid": "10",
      "name": "Millennium Falcon",
      "url": "https://www.swapi.tech/api/starships/10"
    },
    {
      "uid": "13",
      "name": "TIE Advanced x1",
      "url": "https://www.swapi.tech/api/starships/13"
    },
    {
      "uid": "15",
      "name": "Executor",
      "url": "https://www.swapi.tech/api/starships/15"
    },
    {
      "uid": "12",
      "name": "X-wing",
      "url": "https://www.swapi.tech/api/starships/12"
    },
    {
      "uid": "17",
      "name": "Rebel transport",
      "url": "https://www.swapi.tech/api/starships/17"
    }
  ]
}

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
   
    return jsonify(people), 200


# @app.route('/people/<int:people_id>', methods=['GET'])
# def get_character():
    
   
#     return jsonify(response_body), 200


# @app.route('/planets', methods=['GET'])
# def get_planets():
    
   
#     return jsonify(response_body), 200


# @app.route('/planets/<int:planets_id>', methods=['GET'])
# def get_planet():
    
   
#     return jsonify(response_body), 200



# @app.route('/starships', methods=['GET'])
# def get_starships():
    
   
#     return jsonify(response_body), 200

    
# @app.route('/starships/<int:planets_id>', methods=['GET'])
# def get_starship():
    
   
#     return jsonify(response_body), 200


# @app.route('/favourites', methods=['GET'])
# def get_favourites():
    
   
#     return jsonify(response_body), 200



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
