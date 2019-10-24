from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from weather_info.temperature.serializers.validation_serializers import AverageTemperatureRequestSerializer
from weather_info.temperature.temperature_clients.accuweather_client import AccuweatherClient
from weather_info.temperature.temperature_clients.noaa_client import NoaaClient
from weather_info.temperature.temperature_clients.weatherdotcom_client import WeatherdotcomClient


class AverageTemperatureViewSet(APIView):
    default_filters = ['noaa', 'weather.com', 'accuweather']

    def check_valid_filters(self, filter_list):
        return set(filter_list).issubset(set(self.default_filters))

    def post(self, request):
        # Validate input using serializers
        # valid input =
        # {
        #     "latitude": 30.267153, (REQUIRED)
        #     "longitude": -97.743057, (REQUIRED)
        #     "filters": ["accuweather"] (OPTIONAL)
        # }
        serialized_request = AverageTemperatureRequestSerializer(data=request.data)
        if serialized_request.is_valid():
            request_data = serialized_request.validated_data
        else:
            response = {
                'errors': serialized_request.errors
            }
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

        lat = request_data['latitude']
        long = request_data['longitude']
        weather_sources = request_data.get('filters', [])

        # If the optional filter list is not provided, set to the default of ALL the filterable weather services
        if len(weather_sources) == 0:
            weather_sources = self.default_filters

        # Validate filters provided
        if not self.check_valid_filters(weather_sources):
            response = {
                'errors': f'Invalid filters provided. Valid values => {self.default_filters}'
            }
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

        total_temperature = 0

        for weather_source in weather_sources:
            if weather_source == 'accuweather':
                total_temperature += AccuweatherClient().get_temperature(lat=lat, long=long)
            elif weather_source == 'noaa':
                total_temperature += NoaaClient().get_temperature(lat=lat, long=long)
            elif weather_source == 'weather.com':
                total_temperature += WeatherdotcomClient().get_temperature(lat=lat, long=long)

        average_temperature = str(total_temperature / len(weather_sources))

        response = {
            'average_current_temperature': f'{average_temperature} degrees',
            'scale': 'fahrenheit',
            'pulled_from': weather_sources
        }

        return Response(data=response, status=status.HTTP_200_OK)
