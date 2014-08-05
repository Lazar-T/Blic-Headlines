import urllib
from bs4 import BeautifulSoup

page_url = 'http://www.blic.rs/'
page = urllib.urlopen(page_url)
soup = BeautifulSoup(page)


a = soup.find(id="cat_boxes")
b = a.find_all('a')


def worldNewsOne():
    text10 = b[9].text
    href10 = b[8].get('href')
    return text10, href10


def worldNewsTwo():
    text11 = b[11].text
    href11 = b[11].get('href')
    return text11, href11


def worldNewsThree():
    text12 = b[12].text
    href12 = b[12].get('href')
    return text12, href12


def worldNewsFour():
    text13 = b[13].text
    href13 = b[13].get('href')
    return text13, href13
