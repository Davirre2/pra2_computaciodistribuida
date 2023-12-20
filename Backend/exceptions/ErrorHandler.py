from fastapi.responses import JSONResponse as jr

def used_email_exception_handler(request, exc):
    return jr(
        status_code = 400, #TODO maybe mirarse els errors
        content = {"msg" : exc.message},
    )

def auth_exception_handler(request, exc):
    return jr(
        status_code = 401,
        content = {"msg" : exc.message},
    )

def wrong_user_exception_handler(request, exc):
    return jr(
        status_code = 401,
        content = {"msg" : exc.message},
    )

def empty_payload_exception_handler(request, exc):
    return jr(
        status_code = 422,
        content = {"msg" : exc.message},
    )

def empty_response_exception_handler(request, exc):
    return jr(
        status_code = 404,
        content = {"msg" : exc.message},
    )

def nonexistent_id_exception_handler(request, exc):
    return jr(
        status_code=404,
        content = {"msg" : exc.message},
    )