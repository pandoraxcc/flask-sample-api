from core import app
import json
import requests
from flask import Flask, jsonify, request
from models import db, Cities
from helpers import retrive_data, search_nearby

# All cities in the database
@app.route('/', methods = ['GET'])
def home():
    data = Cities.get_cities_list()

    return jsonify({"status":"Succeed", "message": f"{data}"}), 200

# Adding the city
@app.route('/add-city/', methods = ['POST'])
def add_city():
    if request.method == 'POST':
        
        city_name = request.args.get('city')
        # Calling weather API
        data = retrive_data(city_name)

        if data:
            long, lat = data
            status = Cities.add_city(city_name, long, lat)

            if status:
                return jsonify({"status":"Succeed", "message": f"Added the city {city_name}"}), 201

            return jsonify({"status":"Failed", "message": f"Can't add the city, as it already exists {city_name}"}), 400
    
    return jsonify({"status":"Failed", "message": f"Invalid request, only POST requests"}), 400

# Removing the city from the database
@app.route('/remove-city/', methods = ['POST'])
def remove_city():
    if request.method == 'POST':
        
        city_name = request.args.get('city')
        status = Cities.remove_city(city_name)

        if status:
            return jsonify({"status":"Succeed", "message": f"Removed the city {city_name}"}), 200

        return jsonify({"status":"Failed", "message": f"The requested city {city_name} was not registered"}), 400
        
    return jsonify({"status":"Failed", "message": f"Invalid request, accepted only POST request"}), 400

# Get 2 closest cities from the database by long and lat
@app.route('/find-cities/', methods = ['POST'])
def find_cities():
    if request.method == 'POST':

        long = request.args.get('long')
        lat = request.args.get('lat')
        params = [float(long), float(lat)]

        data = Cities.get_cities_list()

        # Including the city used for search
        if len(data) >= 3:

            city1, city2 = search_nearby(params, data)

            return jsonify({"status":"Succeed", "message": f"The nearest cities are {city1, city2}"}), 200
        
        return jsonify({"status":"Failed", "message": f"The database contains less than 2 cities"}), 400
    
    return jsonify({"status":"Failed", "message": f"Invalid request, accepted only POST request"}), 400

if __name__ == '__main__':
    app.run(host='localhost', port=4500)
