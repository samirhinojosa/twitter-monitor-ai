from functools import lru_cache
from pydantic_settings import BaseSettings

class Setting(BaseSettings):

    # General information
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

    # current API version
    API_VERSION: str = "/api/v1"
    FAST_API_VERSION: str = "0.0.1"

@lru_cache
def get_settings():
    return Setting()  