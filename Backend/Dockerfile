FROM python:latest
COPY . .
RUN pip install -r requirements.txt
CMD [ "python3 -m uvicorn main:app --host 127.0.0.1 --port 8000" ]