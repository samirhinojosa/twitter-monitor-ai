from fastapi import APIRouter, Path, Query
from typing import List
from app.domain.schemas.tweet import TweetResponse
from app.infrastructure.services.twitter_service import TwitterScraperService
from app.use_cases.fetch_tweets import FetchTweetsUseCase


router = APIRouter()

@router.get("/tweets/{user_name}", response_model=List[TweetResponse])
def get_user_tweets(
    user_name: str = Path(..., description="Twitter username"),
    max_results: int = Query(10, description="Number of recent tweets to fetch")
):
    service = TwitterScraperService()
    use_case = FetchTweetsUseCase(service)
    return use_case.run(user_name=user_name, keyword="", max_results=max_results)