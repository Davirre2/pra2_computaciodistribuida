from fastapi.responses import JSONResponse as jr

def used_email_exception_handler(request, exc):
    return jr(
        status_code = 400, #TODO maybe mirarse els errors
        content = {"msg" : exc.message},
    )

