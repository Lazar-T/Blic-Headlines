import urllib
from bs4 import BeautifulSoup
import storiesText


text1, href1 = storiesText.firstHeadline()
text2, href2 = storiesText.secondHeadline()
text3, href3 = storiesText.thirdHeadline()
text4, href4 = storiesText.fourthHeadline()
text5, href5 = storiesText.fifthHeadline()

text10, href10 = storiesText.world_story_one()
text11, href11 = storiesText.world_story_two()
text12, href12 = storiesText.world_story_three()
text13, href13 = storiesText.world_story_four()

text14, href14 = storiesText.chronic_story_one()
text15, href15 = storiesText.chronic_story_two()
text16, href16 = storiesText.chronic_story_three()
text17, href17 = storiesText.chronic_story_four()

text18, href18 = storiesText.society_story_one()
text19, href19 = storiesText.society_story_two()
text20, href20 = storiesText.society_story_three()
text21, href21 = storiesText.society_story_four()

text22, href22 = storiesText.economy_story_one()
text23, href23 = storiesText.economy_story_two()
text24, href24 = storiesText.economy_story_three()
text25, href25 = storiesText.economy_story_four()


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
    hoveringText = soup.find(id="article_lead").text
    return hoveringText


def hoverText5():
    page = urllib.urlopen(href5)
    soup = BeautifulSoup(page)
    hoveringText = soup.find(id="article_lead").text
    return hoveringText


def hoverText6():
    page = urllib.urlopen(href10)
    soup = BeautifulSoup(page)
    hoveringText = soup.find(id="article_lead").text
    return hoveringText


def hoverText7():
    page = urllib.urlopen(href11)
    soup = BeautifulSoup(page)
    hoveringText = soup.find(id="article_lead").text
    return hoveringText


def hoverText8():
    page = urllib.urlopen(href12)
    soup = BeautifulSoup(page)
    hoveringText = soup.find(id="article_lead").text
    return hoveringText


def hoverText9():
    page = urllib.urlopen(href13)
    soup = BeautifulSoup(page)
    hoveringText = soup.find(id="article_lead").text
    return hoveringText


def hoverText10():
    page = urllib.urlopen(href14)
    soup = BeautifulSoup(page)
    hoveringText = soup.find(id="article_lead").text
    return hoveringText


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


def hoverText14():
    page = urllib.urlopen(href18)
    soup = BeautifulSoup(page)
    hoveringText = soup.find(id="article_lead").text
    return hoveringText


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


def hoverText18():
    page = urllib.urlopen(href22)
    soup = BeautifulSoup(page)
    hoveringText = soup.find(id="article_lead").text
    return hoveringText


def hoverText19():
    page = urllib.urlopen(href23)
    soup = BeautifulSoup(page)
    hoveringText = soup.find(id="article_lead").text
    return hoveringText


def hoverText20():
    page = urllib.urlopen(href24)
    soup = BeautifulSoup(page)
    hoveringText = soup.find(id="article_lead").text
    return hoveringText


def hoverText21():
    page = urllib.urlopen(href25)
    soup = BeautifulSoup(page)
    hoveringText = soup.find(id="article_lead").text
    return hoveringText
