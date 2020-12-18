from pyowm.owm import OWM
from bocik import token_holder

owm = OWM(token_holder.WEATHER_TOKEN)
mgr = owm.weather_manager()


def get_weather_at_city(city):
    observation = mgr.weather_at_place(city)
    weather = observation.weather
    message_to_send = f"Miasto: {city} \n " \
                      f"Status: {weather.detailed_status.lower()} \n " \
                      f"Temperatura: od {weather.temperature('celsius')['temp_min']} do {weather.temperature('celsius')['temp_max']} °C\n " \
                      f"Obecna temperatura: {weather.temperature('celsius')['temp']} °C"
    return message_to_send

