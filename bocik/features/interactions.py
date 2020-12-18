import random

random.seed()

hello_list = [
    "...",
    "No hejka",
    "BOŻE, ZNOWU TY?!",
    "Witaj przybyszu!",
    "Cześć",
    "Siema",
    "Dzień dobry"
]

bye_list = [
    "Rzegnaj",
    "Do ponownego napisania!",
    "Bywaj",
    "PS: Cyberpunk jest przehajpowany, ale i tak jest dobrą grą, mimo błędów technicznych!",
    "Bywaj zdrów!",
    "Omae wa mou shindeiru"
]

compliment_list = [
    "Ale masz biceps!",
    "Pięknie dziś wyglądasz!",
    "Ściąłeś włosy? Dobrze wyglądasz!",
    "Dobrze, że jesteś!",
    "Nudno jest bez Ciebie na tym serwerze",
]

joke_list = [
    "Javoviec jakimś cudem spłodził dziecko. \nMiał wymyślić imię dla dziecka. Na wszelki wypadek przygotował 2, jakby urodziły się bliźniaki. \nNa nieszczęście urodziły się trojaczki i dostały imiona: Jaś, Staś, ArrayIndexOutOfBoundsException",
    "Spotyka się dwóch programistów: \nSłyszałem, że straciłeś pracę. Jak to jest być bezrobotnym? \nTo było najgorsze pół godziny mojego życia!",
    "Na świecie jest 10 rodzajów ludzi: ci, którzy rozumieją system binarny i ci, którzy go nie rozumieją",
    "Dlaczego programiści mylą Boże Narodzenie z Halloween ?\nBo 25 Dec = 31 Oct",
    "Dlaczego nie można programować w Boże Narodzenie? \n-Bo bug się rodzi"
]


def get_hello():
    return random.choice(hello_list)


def get_bye():
    return random.choice(bye_list)


def get_compliment():
    return random.choice(compliment_list)


def get_joke():
    return random.choice(joke_list)
