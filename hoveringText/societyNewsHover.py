import urllib
from bs4 import BeautifulSoup
import societyNews


text18, href18 = societyNews.societyStoryOne()
text19, href19 = societyNews.societyStoryTwo()
text20, href20 = societyNews.societyStoryThree()
text21, href21 = societyNews.societyStoryFour()


def hoverText14():
    page = urllib.urlopen(href18)
    soup = BeautifulSoup(page)
    hoveringText6 = soup.find(id="article_lead").text
    return hoveringText6


def hoverText15():
    page = urllib.urlopen(href19)
    soup = BeautifulSoup(page)
    hoveringText = soup.find(id="article_lead").text
    return hoveringText


def hoverText16():
    page = urllib.urlopen(href20)
    soup = BeautifulSoup(page)
    hoveringText = soup.find(id="article_lead").text
    return hoveringText


def hoverText17():
    page = urllib.urlopen(href21)
    soup = BeautifulSoup(page)
    hoveringText = soup.find(id="article_lead").text
    return hoveringText
