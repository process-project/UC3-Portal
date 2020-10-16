import os

basedir = os.path.abspath(os.path.dirname(__file__))

#CHANGE FOR PROD
SECRET_KEY = "CHANGESECRETKEY"

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'metadata.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

MAX_DIR_DL_SIZE = 61311272960
