FROM python:3.10-alpine

WORKDIR /app

RUN python -m pip install --upgrade pip

COPY requirements.txt /app/requirements.txt

RUN apk update && apk --no-cache add --virtual bash git gcc g++

RUN pip install -r requirements.txt


COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
