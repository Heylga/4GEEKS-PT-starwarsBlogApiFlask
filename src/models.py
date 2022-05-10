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
            # do not serialize the password, its a security breach
        }

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
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            # do not serialize the password, its a security breach
        }


    #     class Planets(db.Model):
    # __tablename__ = 'planets'

    # id = db.Column(db.Integer, primary_key=True)
    # population = db.Column(db.String(120), nullable=False)
    # terrain = db.Column(db.String(120), nullable=False)

    # def __repr__(self):
    #     return '<Planets %r>' % self.name

    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         "population": self.population,
    #         "terrain": self.terrain,
    #         # do not serialize the password, its a security breach
    #     }


    # class Starships(db.Model):
    # __tablename__ = 'starships'

    # id = db.Column(db.Integer, primary_key=True)
    # model = db.Column(db.String(120), nullable=False)
    # manufacturer = db.Column(db.String(120), nullable=False)

    # def __repr__(self):
    #     return '<Starships %r>' % self.name

    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         "model": self.model,
    #         "manufacturer": self.manufacturer,
    #         # do not serialize the password, its a security breach
    #     }


    # class Favourites(db.Model):
    # __tablename__ = 'favourites'

    # id = db.Column(db.Integer, primary_key=True)
    # favourite_id = db.Column(db.String(120), nullable=False)

    # def __repr__(self):
    #     return '<Favourites %r>' % self.name

    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         "favourite_id": self.favourite_id,
    #         # do not serialize the password, its a security breach
    #     }