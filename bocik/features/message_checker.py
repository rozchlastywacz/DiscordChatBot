import random

from bocik.features.cats import *
from bocik.features.interactions import *
from bocik.features.random_number_generator import *
from bocik.features.weather import get_weather_at_city
from bocik.features.youtube_searching import get_athlean_link


def check_for_dice(message):
    if message.content.find("losuj") != -1 or message.content.find("rzuć") != -1 or message.content.find(
            "rzucić") != -1:
        if message.content.find("kości") != -1 or message.content.find("kość") != -1:
            return throw_a_dice()
    return ""


def check_for_8ball(message):
    if message.content.find("losuj") != -1 or message.content.find("rzuć") != -1 or message.content.find(
            "rzucić") != -1:
        if message.content.find("8ball") != -1 or message.content.find("ball") != -1:
            if message.content.find("czy") != -1 or message.content.find("?") != -1:
                return get_eight_ball()
    return ""


def check_for_coins(message):
    if message.content.find("losuj") != -1 or message.content.find("rzuć") != -1 or message.content.find(
            "rzucić") != -1:
        if message.content.find("moneta") != -1 or message.content.find("monetę") != -1:
            return get_coin_face()
    return ""


def check_for_hello(message):
    if message.content.startswith("hej") or message.content.startswith("cześć") or message.content.startswith(
            "siema") or message.content.startswith("witaj"):
        if message.content.find("bot") != -1 or message.content.find("bocie") != -1:
            return get_hello()
    return ""


def check_for_bye(message):
    if message.content.startswith("żegnaj") or message.content.startswith("papa") or message.content.startswith(
            "do widzenia") or message.content.startswith("dobranoc") or message.content.startswith("dowidzenia") or message.content.startswith("narazie"):
        if message.content.find("bot") != -1 or message.content.find("bocie") != -1:
            return get_bye()
    return ""


def check_for_compliment(message):
    if message.content.find("komplement") != -1 or message.content.find("coś miłego") != -1:
        if message.content.find("mnie") != -1 or message.content.find("mi") != -1:
            return get_compliment()
    return ""


def check_for_joke(message):
    if message.content.find("powiedz") != -1 or message.content.find("zapodaj") != -1:
        if message.content.find("żart") != -1 or message.content.find("kawał") != -1:
            return get_joke()
    return ""


def check_for_bajo_jajo(message):
    if message.content.find("bajo") != -1 or message.content.find("jajo") != -1:
        return f"Ja Ci dam bajo jajo, na {message.channel.name} chamie Ty!\n"
    return ""


def check_for_cats(message):
    if message.content.find("daj") != -1 or message.content.find("zapodaj") != -1:
        if message.content.find("kotka") != -1 or message.content.find("kotki") != -1 or message.content.find(
                "kota") != -1:
            if message.content.find("gif") != -1:
                return get_cat_gif()
            else:
                return get_cat_picture()
    return ""


def check_for_exercise(message):
    if message.content.find("daj") != -1 or message.content.find("zapodaj") != -1 or message.content.find(
            "trening") != -1 or message.content.find("jak zrobić") != -1:
        if message.content.find("biceps") != -1:
            return get_athlean_link("biceps")
        if message.content.find("triceps") != -1:
            return get_athlean_link("triceps")
        if message.content.find("brzuch") != -1:
            return get_athlean_link("abs")
        if message.content.find("klat") != -1:
            return get_athlean_link("chest")
        if message.content.find("nog") != -1:
            return get_athlean_link("legs")
        if message.content.find("bark") != -1:
            return get_athlean_link("shoulder")
    return ""


def check_for_weather(message):
    if message.content.find("podaj") != -1 or message.content.find("zapodaj") != -1 or message.content.find(
            "czy") != -1 or message.content.find("będzie") != -1:
        if message.content.find("pogod") != -1 or message.content.find("ciepło") != -1 or message.content.find(
                "padać") != -1 or message.content.find("śnieg") != -1:
            if message.content.find("krakow") != -1 or message.content.find("kraków") != -1:
                return get_weather_at_city('Krakow, PL')
            if message.content.find("londyn") != -1 or message.content.find("london") != -1:
                return get_weather_at_city('London, GB')
    return ""
