from django.conf import settings
import requests
from rest_framework import status


class WeatherdotcomClient:

    def __init__(self):
        self.noaa_endpoint = f'{settings.WEATHER_API_ENDPOINT}/weatherdotcom'

    # Example request (POST): /weatherdotcom {"lat":33.3,"lon":44.4}
    def get_temperature(self, lat, long):
        request_payload = {'lat': lat, 'lon': long}
        response = requests.post(url=self.noaa_endpoint, json=request_payload)

        # Ensure a successful response before processing result
        if response.status_code != status.HTTP_200_OK:
            raise Exception(f'Invalid response received from Weather.com => {response.__dict__}')

        current_temperature = int(response.json()['query']['results']['channel']['condition']['temp'])
        return current_temperature
