from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import sqlalchemy


# needed by beanstalk
application = Flask(__name__)

# Load the config file
application.config.from_object(Config)
#engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI)

#application.config.from_envvar('MSIA_SETTINGS', silent=True)

# Initialize the database
db = SQLAlchemy(application)