import urllib
from bs4 import BeautifulSoup
import scrapingBlic


text1, href1 = scrapingBlic.firstHeadline()
text2, href2 = scrapingBlic.secondHeadline()
text3, href3 = scrapingBlic.thirdHeadline()
text4, href4 = scrapingBlic.forthHeadline()
text5, href5 = scrapingBlic.fifthHeadline()


def hoverText1():
    page = urllib.urlopen(href1)
    soup = BeautifulSoup(page)
    hoveringText = soup.find(id="article_lead").text
    return hoveringText


def hoverText2():
    page = urllib.urlopen(href2)
    soup = BeautifulSoup(page)
    hoveringText = soup.find(id="article_lead").text
    return hoveringText


def hoverText3():
    page = urllib.urlopen(href3)
    soup = BeautifulSoup(page)
    hoveringText = soup.find(id="article_lead").text
    return hoveringText


def hoverText4():
    page = urllib.urlopen(href4)
    soup = BeautifulSoup(page)
    hoveringText = soup.find(id="article_lead")
    return hoveringText


def hoverText5():
    page = urllib.urlopen(href5)
    soup = BeautifulSoup(page)
    hoveringText = soup.find(id="article_lead").text
    return hoveringText
