import random

from youtubesearchpython import SearchVideos


def get_athlean_link(keyword):
    search = SearchVideos("ATHLEAN-X™", offset=5, mode="dict", max_results=100)
    keyword_link_list = []
    for video in search.result()['search_result']:
        if video['title'].lower().find(keyword) != -1:
            keyword_link_list.append(video['link'])
    if len(keyword_link_list) != 0:
        return random.choice(keyword_link_list)
    else:
        return "Nie mogłem znaleźć takiego filmiku\n"
