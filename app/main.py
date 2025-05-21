from fastapi import FastAPI
from app.core.settings import get_settings
from app.api.v1.routers import twitter

# Runtime Settings/Environment Configuration
settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.DESCRIPTION,
    version=settings.FAST_API_VERSION,
    openapi_url="/openapi.json",
    contact=settings.CONTACT,
    license_info=settings.LICENSE_INFO
)

@app.get("/")
def read_root():
    return {"message": "Twitter Monitor API is live"}


app.include_router(twitter.router, prefix="/api/v1")