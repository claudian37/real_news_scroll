import pandas as pd
import datetime as dt

from bs4 import BeautifulSoup
import requests

class ScraperNYTimes(object):
	def __init__(self):
		pass

	def scrape_site(self, url, element, attribute=None):
		"""
		Function to scrape NYTimes website using BeautifulSoup. It takes the following functions
		- url (str): 'https://www.nytimes.com/section/world'
		- element (str): element to find from scraped results.
		- attribute (str): attribute to find within element from scraped results.

		Returns scraped information in pandas DataFrame
		"""
		response = requests.get(url)
		results = BeautifulSoup(response.text, 'html.parser')

		articles = results.find_all(element)
		all_articles = []

		for article in articles:
			dict_article = {}

			headline = article.find('h2')
			if headline:
				dict_article['headline'] = headline.text.strip()

			link = article.find('h2').find('a')
			if link:
				dict_article['link'] = 'https://www.nytimes.com' + link['href']

			summary = article.find('p')
			if summary:
				dict_article['summary'] = summary.text

			dict_article['updated_time'] = dt.datetime.now().strftime('%Y-%m-%d %H:%m')
			all_articles.append(dict_article)

		df = pd.DataFrame.from_dict(all_articles)

		return df

	def parse_article(self, url, element, attribute=None):
		"""
        Function to parse each article. It takes the following arguments:
        - url (str): links to articles from top headlines scraped returned from scrape_site() function
        - element (str): element to find article from scraped results.

        Returns scraped information as a str.
        """
		response = requests.get(url)
		results = BeautifulSoup(response.text, 'html.parser')
		paragraphs = results.find(element)

		try:
			article = [p.text for p in paragraphs if (p.text != '') and ('advertisement' not in p.text.lower())]
			article = article[1:] 	# Exclude byline at the start
			article = "".join(article)
		except:
			article = None

		return article