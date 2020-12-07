from apscheduler.schedulers.blocking import BlockingScheduler
from utils.scraperBBC import ScraperBBC
from utils.scraperReuters import ScraperReuters
from main import tweet_headlines
import datetime as dt

sched = BlockingScheduler()
bbc_scraper = ScraperBBC()
reuters_scrapper = ScraperReuters()

dict_scrapers = {'scraper': [bbc_scraper, reuters_scrapper],
				 'url': ['https://www.bbc.co.uk/news', 'https://www.reuters.com/news/world'],
				 'element_scraper': ['div', 'div'],
				 'attribute': ['gs-c-promo', 'story-content'],
				 'element_parser': ['article', 'div'],
				 'attribute_parser': [None, 'StandardArticleBody_body']}

@sched.scheduled_job('interval', minutes=5)
# @sched.scheduled_job('cron', day_of_week='mon-sun', hour=12)
def scheduled_job():
	for i in range(2):
		tweet_headlines(scraper=dict_scrapers['scraper'][i], 
						url=dict_scrapers['url'][i], 
						element_scraper=dict_scrapers['element_scraper'][i], 
						attribute=dict_scrapers['attribute'][i], 
						element_parser=dict_scrapers['element_parser'][i], 
						attribute_parser=dict_scrapers['attribute_parser'][i]
						n_headlines=3)
	print('Tweeted at ', dt.datetime.today())

sched.start()
