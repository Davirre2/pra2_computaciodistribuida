import time
import threading
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import database.database as database
import models.home as Home
import services as services

app = FastAPI()

#tokens metadata per els schemas o els routers

database.init_database()

home_data = {
    "home_name": "My Home",
    "home_description": "Description",
    "home_address": "123 Main St",
    "owner": 1,
}

response = requests.post("http://127.0.0.1:8000/home/", json=home_data)
print(response.json())
if response.status_code == 200:
    created_home = response.json()
    print("Home created successfully:")
    print(created_home)

response = request.get("http://127.0.0.1:8000/home/", json=home_data)
print(response.json())