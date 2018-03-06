import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir, 'application.db')
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flasktest:Desktop01@animaloutcomes.c76qrkgxophn.us-east-1.rds.amazonaws.com/animaloutcomes'
    SQLALCHEMY_TRACK_MODIFICATIONS = False