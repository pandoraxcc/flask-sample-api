from key import api_key
import math
import requests


# Call the api endpoint 
def retrive_data(city):
    s = requests.session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-J610FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/282.0.0.40.117;]'
        }
    data = s.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}', headers=headers)
    
    if data.status_code == 200:
        record = data.json()
        return [record['coord']['lon'], record['coord']['lat']]
    
    else:
        return None

# Calculating the nearest cities using great-circle distance:
# https://en.wikipedia.org/wiki/Great-circle_distance
def calculate_distance(params, data):
    # Unpacking the values
    long1, lat1 = params
    city, long2, lat2 = data

    # Transforming the data from degrees to radians
    long1 = math.radians(long1)
    lat1 = math.radians(lat1)

    long2 = math.radians(long2)
    lat2 = math.radians(lat2)

    # Calculating the distance in km
    data = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(long2-long1)) * 6371

    return [city, data]

# Find nearby cities by long nad lat:
def search_nearby(params, data):
    storage = []
    for item in data:
        
        db_data = [item['city_name'], item['long'], item['lat']]
        calc = calculate_distance(params, db_data)

        # If requested city is in the list, skip
        if calc[1] == 0.0:
            continue

        storage.append(calc)

    storage.sort(key=lambda array_city_dist: array_city_dist[1])
    result = [x[0] for x in storage]
            
    return result[:2]