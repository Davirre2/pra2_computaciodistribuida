from fastapi import FastAPI

import services as services
from routers.home import router as routerhome
from routers.user import router as routeruser
from routers.room import router as routerroom


from exceptions import ErrorHandler
from exceptions.UsedEmailException import UsedEmailException

app = FastAPI()

app.add_exception_handler(UsedEmailException, ErrorHandler.used_email_exception_handler)

app.include_router(routerhome, tags=["home"])
app.include_router(routeruser, tags=["user"])
app.include_router(routerroom, tags=["room"])

#tokens metadata per els schemas o els routers




# response = requests.post("http://127.0.0.1:8000/home", json=home_data)
# print(response.json())
# if response.status_code == 200:
#     created_home = response.json()
#     print("Home created successfully:")
#     print(created_home)

# response = requests.get("http://127.0.0.1:8000/home/", json=home_data)
# print(response.json())