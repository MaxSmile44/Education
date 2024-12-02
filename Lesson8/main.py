import json
import os
import requests
from geopy import distance
import folium
from dotenv import load_dotenv


def file_open(file_name):
    with open(file_name, "r", encoding="CP1251") as coffee_file:
        coffee_list = json.loads(coffee_file.read())
        return coffee_list


def fetch_coordinates(apikey, address):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    response = requests.get(base_url, params={
        "geocode": address,
        "apikey": apikey,
        "format": "json",
    })
    response.raise_for_status()
    found_places = response.json()['response']['GeoObjectCollection']['featureMember']

    if not found_places:
        return None

    most_relevant = found_places[0]
    lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
    return lat, lon


def create_new_tuple(file_name, place_coordinates):
    item_final_data = {}
    final_data = []
    for data_coffee in file_open(file_name):
        item_final_data['title'] = data_coffee['Name']
        coffee_coordinates = (data_coffee['geoData']['coordinates'][1], data_coffee['geoData']['coordinates'][0])
        item_final_data['distance'] = distance.distance(place_coordinates, coffee_coordinates).km
        item_final_data['latitude'] = data_coffee['geoData']['coordinates'][1]
        item_final_data['longitude'] = data_coffee['geoData']['coordinates'][0]
        final_data.append(item_final_data)
        item_final_data = {}
    return final_data


def get_distance(final_data):
    return final_data['distance']


def create_map(your_location, markers):
    map = folium.Map(your_location, zoom_start=14)
    for mark in markers:
        folium.Marker(
            location=(mark['latitude'],mark['longitude']),
            tooltip=mark['title'],
            popup=mark['title'],
            icon=folium.Icon(icon="cutlery"),
        ).add_to(map)
    map.save("index.html")


def main(file_name, apikey, address):
    place_coordinates = {fetch_coordinates(apikey, address)}
    sorted_coffee_list = sorted(create_new_tuple(file_name, place_coordinates), key=get_distance)[:5]
    create_map(list(place_coordinates)[0], sorted_coffee_list)
    for nearest_coffee in sorted_coffee_list:
        print(nearest_coffee['title'])


if __name__ == '__main__':
    load_dotenv()
    file_name = 'coffee.json'
    apikey = os.getenv('YANDEX_GEO_API')
    address = input('Где вы находитесь? ')
    main(file_name, apikey, address)