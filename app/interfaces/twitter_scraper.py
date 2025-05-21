from abc import ABC, abstractmethod
from typing import List
from app.domain.models.tweet import TweetModel

class TwitterScraperInterface(ABC):
    @abstractmethod
    def get_user_tweets(self, user_name: str, max_results: int = 5) -> List[TweetModel]:
        pass

