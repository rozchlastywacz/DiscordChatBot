# Returns a random magic 8 Ball message
import random

random.seed()


def throw_a_dice():
    return "Rzuciłem kością D6.\nWylosowałem: " + str(random.randrange(1, 6))


def get_eight_ball():
    eight_ball_messages = ['It is certain',
                           'It is decidedly so',
                           'Without a doubt',
                           'Yes, definitely',
                           'You may rely on it',
                           'As I see it, yes',
                           'Most likely',
                           'Outlook good',
                           'Yes',
                           'Signs point to yes',
                           'Reply hazy, try again',
                           'Ask again later',
                           'Better not tell you now',
                           'Cannot predict now',
                           'Concentrate and ask again',
                           'Don\'t count on it',
                           'My reply is no',
                           'My sources say no',
                           'Outlook not so good',
                           'Very doubtful']

    return "Zapytałem mojego znajomego z Ameryki (naukowca) i napisał:\n" + random.choice(eight_ball_messages)


# Returns random result to a coin flip
def get_coin_face():
    coin_faces = ['Orzeł', 'Reszka']

    return "Rzucam monetę. \n -> " + random.choice(coin_faces)
