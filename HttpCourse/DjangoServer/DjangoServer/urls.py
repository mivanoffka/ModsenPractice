from django.contrib import admin
from django.urls import path

import OpenWeatherRedirector

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forecast/<str:lat>/<str:lon>', OpenWeatherRedirector.views.forecast),
    path('air_pollution/<str:lat>/<str:lon>', OpenWeatherRedirector.views.air_pollution),
    path('weather_for_now/<str:lat>/<str:lon>', OpenWeatherRedirector.views.weather_for_now),
    path('weather_for_time/<str:lat>/<str:lon>/<str:time>', OpenWeatherRedirector.views.weather_for_time),
    path('forbidden/', OpenWeatherRedirector.forbidden),
    path('custom/<str:resource_name>', OpenWeatherRedirector.custom)
]
