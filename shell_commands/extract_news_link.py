#!/srv/homeassistant/bin/python

from bs4 import BeautifulSoup

import requests

def make_soup(url):
    r  = requests.get(url)
    data = r.text
    return BeautifulSoup(data, "html.parser")

base_url = "https://www.bbc.co.uk/programmes/p002vsn1/episodes/player"

episode_url = make_soup(base_url).select("a.block-link__target")[0] \
        .attrs['href']

file_url = make_soup(episode_url).select("a.popup__list__item")[0] \
        .attrs['href']

print(file_url)
