from msiapp import db


# Create a data model for the database to be setup for the app
class hour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.Integer, unique=False, nullable=False)
    hour = db.Column(db.Integer, unique=False, nullable=False)
    weekday = db.Column(db.Integer, unique=False, nullable=False)
    weather_condition = db.Column(db.Integer, unique=False, nullable=False)    
    temp = db.Column(db.Float, unique=False, nullable=False) 
    humid = db.Column(db.Float, unique=False, nullable=False)    
    windspeed = db.Column(db.Float, unique=False, nullable=False) 

    def __repr__(self):
        return '<hour %r>' % self.id


