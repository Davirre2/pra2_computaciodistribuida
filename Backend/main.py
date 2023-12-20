import database.database
from fastapi import FastAPI

import services as services
from routers.home import router as routerhome
from routers.user import router as routeruser
from routers.room import router as routerroom
from routers.authentication import router as routerauth


from exceptions import ErrorHandler
from exceptions.UsedEmailException import UsedEmailException
from exceptions.AuthException import AuthException
from exceptions.WrongUserException import WrongUserException
from exceptions.EmptyPayloadException import EmptyPayloadException
from exceptions.EmptyResponseException import EmptyResponseException

tags_metadata = [
    {
        "name": "home",
        "description": "Operacions amb les cases",
    },
    {
        "name": "room",
        "description": "Operacions amb les habitacions",
    },
    {
        "name": "user",
        "description": "Operacions amb els usuaris/propietaris de les cases",
    },
]

app = FastAPI(title="NigApi", summary="Api per la practica 2", openapi_tags=tags_metadata)

app.add_exception_handler(UsedEmailException, ErrorHandler.used_email_exception_handler)
app.add_exception_handler(AuthException, ErrorHandler.auth_exception_handler)
app.add_exception_handler(WrongUserException, ErrorHandler.wrong_user_exception_handler)
app.add_exception_handler(EmptyPayloadException, ErrorHandler.empty_payload_exception_handler)
app.add_exception_handler(EmptyResponseException, ErrorHandler.empty_response_exception_handler)


app.include_router(routerhome, tags=["home"])
app.include_router(routeruser, tags=["user"])
app.include_router(routerroom, tags=["room"])
app.include_router(routerauth, tags=["authentication"])