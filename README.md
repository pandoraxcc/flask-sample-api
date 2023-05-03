# API boilerplate using Flask and OpenweatherAPI

## Description

My first sample API on Flask. You can add cities, retrieve their geolocation, filter nearby cities based on the distance using Great circle distance formula.

## Setting up the API

1.Install the requirements: pip3 install requirements.txt under your enviroment<br>
2.Get the API key from https://openweathermap.org/api<br>
3.Insert the key to key.py<br>
4.Run the file models.py to initialize the database<br>
5.Run the server python3 main.py<br>
6.Test with tools like POSTMAN or use requests library to send the requests from your terminal

## Usage

localhost/ [GET] - To get the list of cities stored in the database

localhost/add-city/city [POST] - To add the city to the database. Calls openweathermap for geolocation details. 

localhost/remove-city/city [POST] - To remove the city from the database.

localhost/find-cities/long&lat [POST] - To find the cities based on the provided coordinates. 