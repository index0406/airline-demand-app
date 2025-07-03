import requests

def fetch_flight_data(api_key, source, destination):
    url = f"http://api.aviationstack.com/v1/flights?access_key={api_key}&dep_iata={source}&arr_iata={destination}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        return None