from fastapi import FastAPI
from app.routers.insights import router as insights_router

app = FastAPI(title="Shopify Insights Fetcher")

app.include_router(insights_router)