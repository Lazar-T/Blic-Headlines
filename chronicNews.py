import urllib
from bs4 import BeautifulSoup

page_url = 'http://www.blic.rs/'
page = urllib.urlopen(page_url)
soup = BeautifulSoup(page)


a = soup.find(id="cat_boxes")
b = a.find_all('a')


def chronicStoryOne():
    text14 = b[16].text
    href14 = b[15].get('href')
    return text14, href14


def chronicStoryTwo():
    text15 = b[18].text
    href15 = b[18].get('href')
    return text15, href15


def chronicStoryThree():
    text16 = b[19].text
    href16 = b[19].get('href')
    return text16, href16


def chronicStoryFour():
    text17 = b[20].text
    href17 = b[20].get('href')
    return text17, href17
