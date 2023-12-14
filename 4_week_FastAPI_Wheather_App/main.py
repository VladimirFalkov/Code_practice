from fastapi import FastAPI, Request
from utility import fetch_weather

app = FastAPI()


@app.get("/weather")
def read_root(request: Request):
    ip = request.client.host
    return fetch_weather(ip)
