import pandas as pd
import datetime as dt

from bs4 import BeautifulSoup
import requests

class ScraperReuters(object):
	def __init__(self):
		pass

	def scrape_site(self, url, element, attribute):
		"""
		Function to scrape Reuters website using BeautifulSoup. It takes the following arguments:
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
			dict_article['link'] = 'https://www.reuters.com' + link['href']

			summary = article.find('p')
			dict_article['summary'] = summary.text.strip()

			dict_article['updated_time'] = dt.datetime.now().strftime('%Y-%m-%d %H:%m')
			all_articles.append(dict_article)

		df = pd.DataFrame.from_dict(all_articles)

		return df

	def parse_article(self, url, element, attribute):
		"""
		Function to parse each article. It takes the following arguments:
		- url (str): links to articles from top headlines scraped returned from scrape_site() function
		- element (str): element to find article from scraped results.
		- attribute (str): attribute to find within element from scraped results.

		Returns scraped information as a str.
		"""
		response = requests.get(url)
		results = BeautifulSoup(response.text, 'html.parser')
		paragraphs = results.find(element, {'class': attribute})

		article = [a.text for a in paragraphs.find_all('p')]
		article = article[2:-2] 	#Exclude authors
		article = "".join(article)

		return article