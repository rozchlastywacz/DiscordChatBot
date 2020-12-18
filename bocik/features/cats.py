import requests


# Returns a link to a random cat gif
def get_cat_gif():
    cat_gif = requests.get('http://thecatapi.com/api/images/get?format=src&type=gif')
    if cat_gif.status_code == 200:
        cat_gif = cat_gif.url
        return cat_gif

    else:
        return 'Error 404. Website may be down.'


# Returns a link to a random cat picture or cat gif
def get_cat_picture():
    cat_picture = requests.get('http://thecatapi.com/api/images/get.php')
    if cat_picture.status_code == 200:
        cat_picture = cat_picture.url
        return cat_picture

    else:
        return 'Error 404. Website may be down.'
