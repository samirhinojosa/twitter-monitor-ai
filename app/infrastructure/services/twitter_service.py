from typing import List
import tweepy
from app.interfaces.twitter_scraper import TwitterScraperInterface
from app.core.settings import get_settings
from app.domain.schemas.tweet import TweetResponse

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

    def get_user_tweets(self, user_name: str, max_results: int = 5) -> List[TweetResponse]:
        
        tweets: List[TweetResponse] = []

        try:
            user_id = self.client.get_user(username=user_name).data.id
            response = self.client.get_users_tweets(id=user_id, 
                                                    max_results=max_results, 
                                                    tweet_fields=["created_at", "attachments"],
                                                    expansions=["attachments.media_keys"],
                                                    media_fields=["media_key", "type", "url", "preview_image_url"],
                                                    exclude=["retweets", "replies"]
            )

            # getting the tweets
            tweets_response = response.data or []
            media_dict = {
                media["media_key"]: media 
                for media in response.includes.get("media", [])
            } if response.includes and "media" in response.includes else {}
             
            for tweet in tweets_response:
                # getting the medias in the tweet
                media_keys = tweet.data.get("attachments", {}).get("media_keys", [])
                media_urls = []
                for key in media_keys:
                    media = media_dict.get(key)
                    if media:
                        url = media.get("url") or media.get("preview_image_url")
                        if url:
                            media_urls.append(url)

                tweets.append(TweetResponse(
                    id = str(tweet.id),
                    user_name = user_name,
                    content = tweet.text,
                    created_at = str(tweet.created_at),
                    media_urls = media_urls
                ))

        except tweepy.TooManyRequests as e:
            print("\nRate limited. Try again later.")
            print("Reset time:", e.response.headers.get("x-rate-limit-reset"))
            print("Limit:", e.response.headers.get("x-rate-limit-limit"))            
        
        return tweets