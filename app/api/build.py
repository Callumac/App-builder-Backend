from fastapi import APIRouter, HTTPException
from app.models.schemas import AppBuildRequest
from app.services.builder_engine import build_app_code

router = APIRouter()

@router.post("/generate")
async def generate_app(payload: AppBuildRequest):
    try:
        result = build_app_code(payload)
        return {"status": "success", "url": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
