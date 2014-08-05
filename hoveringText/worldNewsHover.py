import urllib
from bs4 import BeautifulSoup
import worldNews



text10, href10 = worldNews.worldNewsOne()
text11, href11 = worldNews.worldNewsTwo()
text12, href12 = worldNews.worldNewsThree()
text13, href13 = worldNews.worldNewsFour()




def hoverText6():
	page = urllib.urlopen(href10)
	soup = BeautifulSoup(page)
	hoveringText6 = soup.find(id="article_lead").text
	return hoveringText6





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

