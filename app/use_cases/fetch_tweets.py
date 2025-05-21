from typing import List
from app.domain.models.tweet import TweetModel
from app.interfaces.twitter_scraper import TwitterScraperInterface


class FetchTweetsUseCase:
    def __init__(self, scraper: TwitterScraperInterface):
        self.scraper = scraper

    def run(self, user_name: List[str], keyword: str = "", max_results: int = 5) -> List[TweetModel]:
        tweets = self.scraper.get_user_tweets(user_name, max_results)
        if keyword:
            tweets = [
                tweet for tweet in tweets
                if keyword.lower() in tweet.content.lower()
            ]
        return tweets  