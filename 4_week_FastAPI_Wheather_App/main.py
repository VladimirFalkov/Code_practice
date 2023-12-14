from fastapi import FastAPI, Request
from utility import get_weather

app = FastAPI()


@app.get("/weather")
def read_root(request: Request):
    ip = request.client.host
    return get_weather(ip)
