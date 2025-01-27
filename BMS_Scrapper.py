import requests
from datetime import datetime, timezone

headers = {
    "client": "STUD_373",
    "x-api-key": "8SvNsBQ9yB6NWNuQQ7mln2fqO7fGwr6Ka1lt9K2L",
    "authorization": "Basic U1RVRF8zNzM6WGIwd1BYWFdiT245",
    "territory": "IN",
    "api-version": "v201",
    "geolocation": "12.9716;77.5946",  # Latitude and longitude of Bangalore
    "device-datetime": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")  # Current UTC time in ISO 8601 format
}
params =\
    {
    "n": 10
}
api_url = "https://api-gate2.movieglu.com/filmsNowShowing/"
response = requests.get(api_url, headers=headers, params=params)
data = response.json()

#Makes a list of the movies available
movies_list = []
for film in data.get("films", []):
    movies_list.append(film.get("film_name"))
print(movies_list)

result = ['Sky Force', 'Sankrathiki Vasthunam', 'Ramayana: The Legend of Prince Rama', 'Daaku Maharaaj', 'Emergency (Hindi)', 'Pushpa 2: The Rule', "Dominic and the Ladies' Purse", 'Game Changer', 'Kudumbasthan', 'Twilight of the Warriors: Walled In']