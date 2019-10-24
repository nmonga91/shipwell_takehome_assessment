from rest_framework import serializers


class AverageTemperatureRequestSerializer(serializers.Serializer):
    latitude = serializers.FloatField(required=True)
    longitude = serializers.FloatField(required=True)
    filters = serializers.ListField(
        required=False,
        child=serializers.CharField(allow_null=False, allow_blank=False)
    )
