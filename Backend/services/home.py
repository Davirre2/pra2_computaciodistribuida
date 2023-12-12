#aquí hi ha les consultes a BD i tal
import schemas.home
import models.home

@app.get("/get_home_list")
def get_home_list():
    data_to_send = {
        'task_name': current_task.task_name,
        'completion_percent': current_task.completion_percent
    }
    return data_to_send