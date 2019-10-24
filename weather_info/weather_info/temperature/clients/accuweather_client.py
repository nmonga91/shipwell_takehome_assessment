from django.conf import settings
import requests
from rest_framework import status


class AccuweatherClient:

    def __init__(self):
        self.noaa_endpoint = f'{settings.WEATHER_API_ENDPOINT}/accuweather'

    # Example request: /accuweather?latitude=44&longitude=33
    def get_temperature(self, lat, long):
        query_params = {'latitude': lat, 'longitude': long}
        response = requests.get(url=self.noaa_endpoint, params=query_params)

        # Ensure a successful response before processing result
        if response.status_code != status.HTTP_200_OK:
            raise Exception(f'Invalid response received from Accuweather => {response.__dict__}')

        current_temperature = int(response.json()['simpleforecast']['forecastday'][0]['current']['fahrenheit'])
        return current_temperature
