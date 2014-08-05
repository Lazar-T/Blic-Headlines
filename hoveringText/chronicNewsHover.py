import urllib
from bs4 import BeautifulSoup
import chronicNews


text14, href14 = chronicNews.chronicStoryOne()
text15, href15 = chronicNews.chronicStoryTwo()
text16, href16 = chronicNews.chronicStoryThree()
text17, href17 = chronicNews.chronicStoryFour()


def hoverText10():
    page = urllib.urlopen(href14)
    soup = BeautifulSoup(page)
    hoveringText6 = soup.find(id="article_lead").text
    return hoveringText6


def hoverText11():
    page = urllib.urlopen(href15)
    soup = BeautifulSoup(page)
    hoveringText = soup.find(id="article_lead").text
    return hoveringText


def hoverText12():
    page = urllib.urlopen(href16)
    soup = BeautifulSoup(page)
    hoveringText = soup.find(id="article_lead").text
    return hoveringText


def hoverText13():
    page = urllib.urlopen(href17)
    soup = BeautifulSoup(page)
    hoveringText = soup.find(id="article_lead").text
    return hoveringText
