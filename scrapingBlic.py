import urllib
from bs4 import BeautifulSoup


page_url = 'http://www.blic.rs/'
page = urllib.urlopen(page_url)
soup = BeautifulSoup(page)


def firstHeadline():
    text1 = soup.select("#home_main_article_text")[0].h1.text
    href1 = soup.select("#home_main_article_text")[0].a.get('href')
    return text1, href1


def secondHeadline():
    text2 = soup.select("#home_main_article_text")[1].h1.text
    href2 = soup.select("#home_main_article_text")[1].a.get('href')
    return text2, href2


def thirdHeadline():
    text3 = soup.select("#home_main_article_text")[2].h1.text
    href3 = soup.select("#home_main_article_text")[2].a.get('href')
    return text3, href3


def forthHeadline():
    text4 = soup.select("#home_main_article_text")[3].h1.text
    href4 = soup.select("#home_main_article_text")[3].a.get('href')
    return text4, href4


def fifthHeadline():
    text5 = soup.select("#home_main_article_text")[4].h1.text
    href5 = soup.select("#home_main_article_text")[4].a.get('href')
    return text5, href5
