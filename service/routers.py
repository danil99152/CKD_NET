from fastapi import APIRouter
from starlette.responses import JSONResponse

from service.api import ModelApi

router = APIRouter(prefix='/ckd', tags=['ckd'])
api = ModelApi()


@router.get('/ping', response_class=JSONResponse)
async def ping():
    response = api.ping()
    return response


@router.post('/get-result/', response_class=JSONResponse)
async def get_result(data: dict) -> float | dict | str:
    try:
        response = await api.analyse(data)
        return response
    except Exception as e:
        return f'Exception at upload_matrix: {e}'
