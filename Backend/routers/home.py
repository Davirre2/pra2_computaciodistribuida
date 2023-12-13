from fastapi import APIRouter
import Backend.schemas.home as schemas
import Backend.services.home as services

router = APIRouter(
    prefix="/home",
    tags=["home"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def list_home(home_id: id, payload: schemas.HomeList):
    return await services.get_home_list(id, payload)