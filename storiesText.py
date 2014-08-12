import urllib
from bs4 import BeautifulSoup

page_url = 'http://www.blic.rs/'
page = urllib.urlopen(page_url)
soup = BeautifulSoup(page)


a = soup.find(id="cat_boxes")
b = a.find_all('a')


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


def world_story_one():
    text10 = b[9].text
    href10 = b[8].get('href')
    return text10, href10


def world_story_two():
    text11 = b[11].text
    href11 = b[11].get('href')
    return text11, href11


def world_story_three():
    text12 = b[12].text
    href12 = b[12].get('href')
    return text12, href12


def world_story_four():
    text13 = b[13].text
    href13 = b[13].get('href')
    return text13, href13


def chronic_story_one():
    text14 = b[16].text
    href14 = b[15].get('href')
    return text14, href14


def chronic_story_two():
    text15 = b[18].text
    href15 = b[18].get('href')
    return text15, href15


def chronic_story_three():
    text16 = b[19].text
    href16 = b[19].get('href')
    return text16, href16


def chronic_story_four():
    text17 = b[20].text
    href17 = b[20].get('href')
    return text17, href17


def society_story_one():
    text18 = b[23].text
    href18 = b[22].get('href')
    return text18, href18


def society_story_two():
    text19 = b[25].text
    href19 = b[25].get('href')
    return text19, href19


def society_story_three():
    text20 = b[26].text
    href20 = b[26].get('href')
    return text20, href20


def society_story_four():
    text21 = b[27].text
    href21 = b[27].get('href')
    return text21, href21


def economy_story_one():
    text22 = b[30].text
    href22 = b[29].get('href')
    return text22, href22


def economy_story_two():
    text23 = b[32].text
    href23 = b[32].get('href')
    return text23, href23


def economy_story_three():
    text24 = b[33].text
    href24 = b[33].get('href')
    return text24, href24


def economy_story_four():
    text25 = b[34].text
    href25 = b[34].get('href')
    return text25, href25
