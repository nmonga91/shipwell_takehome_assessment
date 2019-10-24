# Nipun's Shipwell Takehome Assessment

## Assumptions:
1. There are no dependent migrations since no data is persisted
2. Only Fahrenheit temperature scale is retrieved due to limitations with the Weather.com mock API response

## Starting the Application:
1. `virtualenv env && source env/bin/activate`
2. `cd weather_info/`
3. `pip install -r requirements.txt`
4. `python manage.py runserver`
	* App will start on `http://localhost:8000/`

## API Documentation:

### Temperature Average
**Route:** `/api/temperature/average/`

**Method:** `POST`

### Request Parameters

1. `latitude` (Type: Long, Required: False): Latitude for which to retrieve average temperature
2. `longitude` (Type: Long, Required: False): Longitude for which to retrieve average temperature
3. `zip_code` (Type: Integer, Required: False): Zip code for which to derive latitude and longitude
4. `filters` (Type: List of Strings, Required: False): List of weather services to filter on. If 
this parameter is not present or is an empty list, it will default to using ALL the weather services.
Valid weather services => ["noaa", "weather.com", "accuweather"].

**Note**: If latitude, longitude, AND zip_code are provided, latitude and longitude will be used. If latitude or longitude are not provided, zip_code will be required.

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
