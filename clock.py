from apscheduler.schedulers.blocking import BlockingScheduler
from main import tweet_headlines
import datetime as dt

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=12)
def scheduled_job():
	tweet_headlines()
	print('Tweeted at ', dt.datetime.today())

sched.start()
