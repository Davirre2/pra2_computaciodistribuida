import time
import threading
from fastapi import FastAPI
from pydantic import BaseModel
from threading import Event

app = FastAPI()
exit_event = Event()

@app.on_event("shutdown")
def shutdown_event():
    exit_event.set()

@app.get("/get_home_list")
def get_home_list():
    data_to_send = {
        'task_name': current_task.task_name,
        'completion_percent': current_task.completion_percent
    }
    return data_to_send

class Data(BaseModel):
    item : str

@app.post("/add_item")
def add_item(data: Data):
    if data.item:
        queue.put(data.item)
        return f'Item added to the queue: {data.item}'
    else:
        return "Item is empty"

@app.get("/get_queue")
def get_queue():
    return list(queue.queue)

wait_thread = threading.Thread(target=waiting_for_queue, args=(current_task,))
wait_thread.start()
    