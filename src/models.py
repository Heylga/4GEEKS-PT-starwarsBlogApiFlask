from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }
 
    def get_user(email, password):
        user = User.query.filter_by(email=email, password=password).first()
        return user
    
    def create_user(email, password):
        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()

class People(db.Model):
    __tablename__ = 'people'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(120), nullable=False)
    hair_color = db.Column(db.String(120), nullable=False)
    eye_color = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "uid": self.uid,
            "name": self.name,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
        }

    def create_people(name, gender, hair_color, eye_color):
        people = People(name=name, gender=gender, hair_color=hair_color, eye_color=eye_color)
        db.session.add(people)
        db.session.commit()

    def get_people(uid):
        people = People.query.filter_by(uid=uid).first()
        return People.serialize(people)

    def get_all_people():
        all_people = People.query.all()
        all_people = list(map(lambda people: people.serialize(), all_people))
        return all_people

    def delete_people(uid):
        people = People.query.get(uid)
        db.session.delete(people)
        db.session.commit()

class Planets(db.Model):
    __tablename__ = 'planets'

    uid = db.Column(db.Integer, primary_key=True)
    population = db.Column(db.String(120), nullable=False)
    terrain = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "uid": self.id,
            "population": self.population,
            "terrain": self.terrain,
        }


    def create_planets(population, terrain):
        planets = Planets(population=population, terrain=terrain)
        db.session.add(planets)
        db.session.commit()

    def get_planets(uid):
        planets = Planets.query.filter_by(uid=uid).first()
        return Planets.serialize(planets)

    def get_all_planets():
        all_planets = Planets.query.all()
        all_planets = list(map(lambda planets: planets.serialize(), all_planets))
        return all_planets

    def delete_planets(uid):
        planets = Planets.query.get(uid)
        db.session.delete(planets)
        db.session.commit()

class Starships(db.Model):
    __tablename__ = 'starships'

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(120), nullable=False)
    manufacturer = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Starships %r>' % self.name

    def serialize(self):
        return {
            "uid": self.id,
            "model": self.model,
            "manufacturer": self.manufacturer,
        }

    def create_starships(model, manufacturer):
        starships = Starships(model=model, manufacturer=manufacturer)
        db.session.add(starships)
        db.session.commit()

    def get_starships(uid):
        starships = Starships.query.filter_by(uid=uid).first()
        return Starships.serialize(starships)

    def get_all_starships():
        all_starships = Starships.query.all()
        all_starships = list(map(lambda starships: starships.serialize(), all_starships))
        return all_starships

    def delete_starships(uid):
        starships = Starships.query.get(uid)
        db.session.delete(starships)
        db.session.commit()

class Favourites(db.Model):
    __tablename__ = 'favourites'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(120), nullable=False)
    favouritetype = db.Column(db.String(120), nullable=False)
    # favourite_character = db.Column(db.String(120), db.ForeignKey(Parent.id))
    # favourite_planet = db.Column(db.String(120), db.ForeignKey(Parent.id))
    # favourite_starship = db.Column(db.String(120), db.ForeignKey(Parent.id))
    favourite_id = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Favourites %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "favouritetype": self.favouritetype,
            "favourite_id": self.favourite_id,
        }


    @classmethod
    def get_all(cls):
        users = cls.query.all()
        return users