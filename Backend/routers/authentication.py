from fastapi import APIRouter
from services.authentication import AuthService
from database.database import db_get

router = APIRouter(
    prefix="/auth",
    tags=["authentication"],
    responses={404: {"description": "Not found"}},
)
auth_service = AuthService(db_get())
@router.get('/login/')
def login(email: str, password: str):
    token = auth_service.login(email, password)
    return {
        "status" : "SUCCESS",
        "data" : token
        }
