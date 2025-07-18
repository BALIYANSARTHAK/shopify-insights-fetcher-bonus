from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.scraper import fetch_shopify_insights

router = APIRouter()

class RequestModel(BaseModel):
    website_url: str

@router.post("/get_insights")
def get_insights(request: RequestModel):
    try:
        data = fetch_shopify_insights(request.website_url)
        if not data:
            raise HTTPException(status_code=404, detail="No data found")
        return {"status": "success", "data": data}
    except ValueError as ve:
        raise HTTPException(status_code=401, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))