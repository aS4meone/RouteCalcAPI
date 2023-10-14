import requests

from config import API_KEY


def get_location(location: str):
    get_url = f'https://graphhopper.com/api/1/geocode?key={API_KEY}&q={location}&provider=default&locale=ru&osm_tag=%21place%3Acounty&osm_tag=%21boundary&osm_tag=%21historic'

    response = requests.get(get_url)

    data = response.json()

    if data and 'hits' in data and len(data['hits']) > 0:
        first_hit = data['hits'][0]
        lat = first_hit['point']['lat']
        lng = first_hit['point']['lng']
        return [lng, lat]


def get_route(start_points, end_points):
    post_url = "https://graphhopper.com/api/1/route"
    query = {
        "key": f"{API_KEY}"
    }
    payload = {
        "points": [start_points, end_points],
        "vehicle": "car",
        "locale": "en",
        "instructions": True,
        "calc_points": True,
        "points_encoded": False
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(post_url, json=payload, headers=headers, params=query)

    data = response.json()

    instructions = data['paths'][0]['instructions']

    instruction_texts = [instruction['text'] for instruction in instructions if 'text' in instruction]

    route_data = {
        'instructions': instruction_texts,
    }

    return route_data
