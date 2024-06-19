from django.http import HttpResponse
import requests


API_TOKEN = 'e1efa5a63bac4c00eae146c8240d755b'
WEATHER_FOR_NOW_TEMPLATE = "https://api.openweathermap.org/data/3.0/onecall?lat={}&lon={}&appid={}"
WEATHER_FOR_TIME_TEMPLATE = ("https://api.openweathermap.org/data/3.0/onecall/"
                             "timemachine?lat={l}&lon={}&dt={}&appid={}")
FORECAST_TEMPLATE = "https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={}&lon={}&appid={}"
AIR_POLLUTION_TEMPLATE = "https://api.openweathermap.org/data/2.5/air_pollution?lat={}&lon={}&appid={}"
FORBIDDEN_TEMPLATE = "https://openweathermap.org/.htaccess"
CUSTOM_TEMPLATE = "https://api.openweathermap.org/{}"


def custom(request, resource_name):
    return get_http_response(CUSTOM_TEMPLATE.format(resource_name.replace("|", "/")))


def forbidden(request):
    return get_http_response(FORBIDDEN_TEMPLATE)


def air_pollution(request, lat, lon):
    return get_http_response(AIR_POLLUTION_TEMPLATE.format(lat, lon, API_TOKEN))


def forecast(request, lat, lon):
    return get_http_response(FORECAST_TEMPLATE.format(lat, lon, API_TOKEN))


def weather_for_now(request, lat, lon):
    return get_http_response(WEATHER_FOR_NOW_TEMPLATE.format(lat, lon, API_TOKEN))


def weather_for_time(request, lat, lon, time):
    return get_http_response(WEATHER_FOR_TIME_TEMPLATE.format(lat, lon, time, API_TOKEN))


def get_http_response(uri):
    response = requests.get(uri)
    return HttpResponse(f"{response.status_code} - this is the status-code Django received from OpenWeather API.")
