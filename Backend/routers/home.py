from fastapi import APIRouter
import schemas.home as schemas
import services.home as services

router = APIRouter(
    prefix="/home",
    tags=["home"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/{id}")
async def list_home(id: int, payload: schemas.HomeList):
    return await services.get_home_list(id, payload)

@router.get("/")
async def list_home(payload: schemas.HomeList):
    return await services.get_home_list(1, payload)