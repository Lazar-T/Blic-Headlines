import urllib
from bs4 import BeautifulSoup
import economyNews



text22, href22 = economyNews.economyStoryOne()
text23, href23 = economyNews.economyStoryTwo()
text24, href24 = economyNews.economyStoryThree()
text25, href25 = economyNews.economyStoryFour()


def hoverText18():
	page = urllib.urlopen(href22)
	soup = BeautifulSoup(page)
	hoveringText6 = soup.find(id="article_lead").text
	return hoveringText6





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
