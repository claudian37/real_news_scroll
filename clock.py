from apscheduler.schedulers.blocking import BlockingScheduler
from main import tweet_headlines

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def scheduled_job():
	tweet_headlines()
	print('Tweeted')

sched.start()
