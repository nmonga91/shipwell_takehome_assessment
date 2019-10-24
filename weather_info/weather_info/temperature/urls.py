from django.conf.urls import url

from weather_info.temperature.views import AverageTemperatureViewSet

urlpatterns = [
    url(r'^average', AverageTemperatureViewSet.as_view())
]