from msiapp import db
from msiapp.models import hour
import os


# Creates a table in the database provided as the 'SQLALCHEMY_DATABASE_URI'
# configuration parameter in __init__.py with the schema defined by models.hour()

#SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
#db.create_engine(SQLALCHEMY_DATABASE_URI)

#def create_db():
print("db created")
db.create_all()
    #hour_describe1 = hour(month= '1', hour= '7', weekday= '5', weather_condition ='2', temp = '27', humid = '70', windspeed = '15')
    #hour_describe2 = hour(month= '2', hour= '5', weekday= '5', weather_condition ='2', temp = '27', humid = '70', windspeed = '15')
    #db.session.add(hour_describe1)
    #db.session.add(hour_describe2)
    
    #db.session.commit()

#if __name__ == "__main__":
#create_db()
