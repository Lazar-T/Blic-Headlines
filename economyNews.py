import urllib
from bs4 import BeautifulSoup

page_url = 'http://www.blic.rs/'
page = urllib.urlopen(page_url)
soup = BeautifulSoup(page)


a = soup.find(id="cat_boxes")
b = a.find_all('a')


def economyStoryOne():
    text22 = b[30].text
    href22 = b[29].get('href')
    return text22, href22


def economyStoryTwo():
    text23 = b[32].text
    href23 = b[32].get('href')
    return text23, href23


def economyStoryThree():
    text24 = b[33].text
    href24 = b[33].get('href')
    return text24, href24


def economyStoryFour():
    text25 = b[34].text
    href25 = b[34].get('href')
    return text25, href25
