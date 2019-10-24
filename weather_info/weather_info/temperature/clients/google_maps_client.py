import googlemaps
from django.conf import settings


class GoogleMapsClient:

    def __init__(self):
        self.gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

    def validate_lat_long(self, lat, long):
        try:
            result = len(self.gmaps.reverse_geocode((lat, long))) >= 1
        except googlemaps.exceptions.HTTPError:
            result = False
        return result

    def get_lat_long_from_zip(self, zip_code):
        results = self.gmaps.geocode(zip_code)
        lat_long = {}

        if len(results) == 0:
            return lat_long

        lat_long['lat'] = results[0]['geometry']['location']['lat']
        lat_long['long'] = results[0]['geometry']['location']['lng']

        return lat_long
