from core import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Cities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(20), unique=True, nullable=False)
    long = db.Column(db.Float, nullable=False)
    lat = db.Column(db.Float, nullable=False)

    @staticmethod
    def get_cities_list():
        cities = Cities.query.all()
        data = [{key: value for key, value in city.__dict__.items() if key != '_sa_instance_state'} for city in cities]
        return data

    @staticmethod
    def query_city(city):
        city = Cities.query.filter_by(city_name=city).first()
        return city

    @staticmethod
    def add_city(city,long,lat):
        query_city = Cities.query_city(city)
        if not query_city:
            city = Cities(city_name=city, long=long, lat=lat)
            db.session.add(city)
            db.session.commit()
            return True
        return False

    @staticmethod
    def remove_city(city):
        query_city = Cities.query_city(city)
        if query_city:
            db.session.delete(query_city)
            db.session.commit()
            return True
        return False

if __name__  == '__main__':
    with app.app_context():
        db.create_all()
