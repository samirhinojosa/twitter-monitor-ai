from typing import List
import tweepy
from app.interfaces.twitter_scraper import TwitterScraperInterface
from app.core.settings import get_settings
from app.domain.models.tweet import TweetModel

# Runtime Settings/Environment Configuration
settings = get_settings()

class TwitterScraperService(TwitterScraperInterface):
    def __init__(self):
        self.client = tweepy.Client(
            consumer_key=settings.X_API_KEY,
            consumer_secret=settings.X_API_KEY_SECRET,
            bearer_token=settings.X_BEARER_TOKEN,
            access_token=settings.X_ACCESS_TOKEN,
            access_token_secret=settings.X_ACCESS_TOKEN_SECRET
        )

    def get_user_tweets(self, user_name: str, max_results: int = 5) -> List[TweetModel]:
        
        tweets: List[TweetModel] = []

        try:
            user_id = self.client.get_user(username=user_name).data.id
            user_tweets = self.client.get_users_tweets(id=user_id, 
                                                    max_results=max_results, 
                                                    tweet_fields=["created_at"])
            for tweet in user_tweets:
                print(f"Tweet: {tweet}")
                # if "media" in tweet.entities:
                if hasattr(tweet, "media"):
                    media = tweet.entities.get("media", [])
                    media_urls = [item["media_url_https"] for item in media] if media else None

                tweets.append(TweetModel(
                    id=tweet.id_str,
                    user_name=tweet.user.screen_name,
                    content=tweet.full_text,
                    created_at=tweet.created_at,
                    media_urls=media_urls
                ))

        except tweepy.TooManyRequests as e:
            print("\nRate limited. Try again later.")
            print("Reset time:", e.response.headers.get("x-rate-limit-reset"))
            print("Limit:", e.response.headers.get("x-rate-limit-limit"))            
        
        return tweets