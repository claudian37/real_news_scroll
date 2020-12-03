import pandas as pd
import datetime as dt

from bs4 import BeautifulSoup
import requests

class ScraperReuters(object):
	def __init__(self):
		pass

	def scrape_site(self, url, element, attirbute):
		"""
		Function to scrape Reuters website using BeautifulSoup. It takes the following functions
		- url (str): 'https://www.reuters.com/news/world' 
		- element (str):element to find from scraped results.
		- attribute (str): attribute to find within element from scraped results.

		Returns scraped information in pandas DataFrame
		""" 
		response = requests.get(url)
		results = BeautifulSoup(response.text, 'html.parser')

		articles = results.find_all(element, {'class': attribute})
		all_articles = []

		for article in articles:
			dict_article = {}

			headline = article.find('h3')
			dict_article['headline'] = headline.text.strip()

			link = article.find('a')
			dict_article['link'] = url + link['href']

			summary = article.find('p')
			dict_article['summary'] = summary.text.strip()

			dict_article['updated_time'] = dt.datetime.now().strftime('%Y-%m-%d %H:%m')
			all_articles.append(dict_article)

		df = pd.DataFrame.from_dict(all_articles)

		return df

	def parse_article(url, element, attribute):
		response = requests.get(url)
		results = BeautifulSoup(response.text, 'html.parser')
		paragraphs = results.find(element, {'class': attribute})

		try:
			article = [a.text for a in paragraphs.find_all('p')]
			article = article[:-1] #Exclude authors at the end
			article = "".join(article)
		except:
			article = None

		return article