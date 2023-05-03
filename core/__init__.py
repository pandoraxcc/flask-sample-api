from flask import Flask
import os

basedir = os.getcwd()
app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{basedir}/cities.sqllite"
