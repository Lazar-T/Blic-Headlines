import urllib
from bs4 import BeautifulSoup

page_url = 'http://www.blic.rs/'
page = urllib.urlopen(page_url)
soup = BeautifulSoup(page)


a = soup.find(id="cat_boxes")
b = a.find_all('a')


def societyStoryOne():
    text18 = b[23].text
    href18 = b[22].get('href')
    return text18, href18


def societyStoryTwo():
    text19 = b[25].text
    href19 = b[25].get('href')
    return text19, href19


def societyStoryThree():
    text20 = b[26].text
    href20 = b[26].get('href')
    return text20, href20


def societyStoryFour():
    text21 = b[27].text
    href21 = b[27].get('href')
    return text21, href21
