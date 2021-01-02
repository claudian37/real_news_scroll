from apscheduler.schedulers.blocking import BlockingScheduler
from utils.scraperBBC import ScraperBBC
from utils.scraperReuters import ScraperReuters
from utils.scraperNYTimes import  import ScraperNYTimes
from main import tweet_headlines
import datetime as dt

sched = BlockingScheduler()

all_scrapers = [
    {
        'scraper': ScraperBBC(),
        'url': 'https://www.bbc.co.uk/news',
        'element_scraper': 'div',
        'attribute': 'gs-c-promo',
        'element_parser': 'article',
        'attribute_parser': None
     },
    {
        'scraper': ScraperReuters(),
        'url': 'https://www.reuters.com/news/world',
        'element_scraper': 'div',
        'attribute': 'story-content',
        'element_parser': 'div',
        'attribute_parser': 'ArticleBodyWrapper'
     },
    {
        'scraper': ScraperNYTimes(),
        'url': 'https://www.nytimes.com/section/world',
        'element_scraper': 'article',
        'attribute': None,
        'element_parser': 'article',
        'attribute_parser': None
     }
]

# @sched.scheduled_job('interval', minutes=5)
@sched.scheduled_job('cron', day_of_week='mon-sun', hour=12)
def scheduled_job():
	for i in range(len(all_scrapers)):
		tweet_headlines(scraper=all_scrapers[i]['scraper'],
						url=all_scrapers[i]['url'],
						element_scraper=all_scrapers[i]['element_scraper'],
						attribute=all_scrapers[i]['attribute'],
						element_parser=all_scrapers[i]['element_parser'],
						attribute_parser=all_scrapers[i]['attribute_parser'],
						n_headlines=3)
	print('Tweeted at ', dt.datetime.today())

sched.start()
