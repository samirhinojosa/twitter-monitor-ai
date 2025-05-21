import os
from dotenv import load_dotenv
from functools import lru_cache
from pydantic_settings import BaseSettings

# load .env
load_dotenv(override=True)

class Setting(BaseSettings):

    # General API information
    APP_NAME: str = "Twetter (now X) Monitor API"
    DESCRIPTION: str = """Twitter (now X) Monitor AI is an intelligent service that monitors and analyzes tweets in real time.<br/>
    It is designed with Clean Architecture principles and built using FastAPI and Docker, ensuring maintainability, scalability, and modularity."""
    OPENAPI_URL: str = "/openapi.json"
    CONTACT: dict = {
        "name": "Samir Hinojosa",
        "url": "https://github.com/samirhinojosa",
        "email": "samirhinojosa@gmail.com",
    }
    LICENSE_INFO: dict = {
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }

    ## current API version
    API_VERSION: str = "/api/v1"
    FAST_API_VERSION: str = "0.0.1"

    # Twitter (now X) data
    X_API_KEY: str
    X_API_KEY_SECRET: str
    X_BEARER_TOKEN: str
    X_ACCESS_TOKEN: str
    X_ACCESS_TOKEN_SECRET: str

    class Config:
        env_file = ".env"    

@lru_cache
def get_settings():
    return Setting()  