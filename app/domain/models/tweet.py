from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class TweetModel(BaseModel):
    id: str
    user_name: str
    content: str
    created_at: Optional[datetime]
    media_urls: Optional[List[str]] = None 