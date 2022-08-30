from multiprocessing.pool import ApplyResult
from psaw import PushshiftAPI
import datetime

api = PushshiftAPI()

start_time = int(datetime.datetime(2022, 8, 28).timestamp())

submissions = list(api.search_submissions(after=start_time,
                            subreddit='sportsbook',
                            filter=['url','author', 'title', 'subreddit'],
                            limit=100))

for submission in submissions:
    print(submission.title)
    apple 

    