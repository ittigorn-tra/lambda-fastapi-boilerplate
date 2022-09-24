from fastapi.routing import APIRouter, Request
from settings import logger
from src.v1.interfaces.serializers.api_status import ApiStatusSerializer

router = APIRouter()


# Health check
@router.get("", response_model=ApiStatusSerializer, tags=['Status'])
async def api_status(request: Request):
    '''
    This endpoint yields the status of this API
    '''
    logger.info(f'An endpoint was called : /status')
    return ApiStatusSerializer(**{
        "title": request.app.title,
        "description": request.app.description,
        "version": request.app.version,
    })
