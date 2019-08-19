#!/config/script-env/bin/python

from bs4 import BeautifulSoup

import requests

def make_soup(url):
    r  = requests.get(url)
    data = r.text
    return BeautifulSoup(data, "html.parser")

base_url = "https://taranakialpineclub.co.nz/cam-support/tac/get-camera-image.php?webcamNumber=3"

image_url = make_soup(base_url).img['src']

print(image_url)
