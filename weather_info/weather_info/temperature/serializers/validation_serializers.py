from rest_framework import serializers


class AverageTemperatureRequestSerializer(serializers.Serializer):
    latitude = serializers.FloatField(required=False)
    longitude = serializers.FloatField(required=False)
    zip_code = serializers.IntegerField(required=False)
    filters = serializers.ListField(
        required=False,
        child=serializers.CharField(allow_null=False, allow_blank=False)
    )
