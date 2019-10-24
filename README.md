# Nipun's Shipwell Takehome Assessment

## Assumptions:
1. There are no dependent migrations since no data is persisted
2. Only Fahrenheit temperature scale is retrieved due to limitations with the Weather.com mock API response

## Starting the Application:
1. `cd weather_info/ && python manage.py runserver`
2. App will start on `http://localhost:8000/`

## API Documentation:

### Temperature Average
**Route:** `/api/temperature/average/`

**Method:** `POST`

### Request Parameters

1. `latitude` (Type: Long, Required: True): Latitude for which to retrieve average temperature
2. `longitude` (Type: Long, Required: True): Longitude for which to retrieve average temperature
3. `filters` (Type: List of Strings, Required: False): List of weather services to filter on. If 
this parameter is not present or is an empty list, it will default to using ALL the weather services.
Valid weather services => ["noaa", "weather.com", "accuweather"].

#### Sample Request (JSON)
```
{
  "latitude": 44,
  "longitude": 33,
  "filters": ["accuweather"]
}
```

### Response (JSON)

```
{
  "average_current_temperature": "55.0 degrees",
  "scale": "fahrenheit",
  "pulled_from": [
    "accuweather"
  ]
}
```
