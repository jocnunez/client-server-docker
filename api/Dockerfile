FROM python:3.9.21-alpine3.20

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

COPY ./src .

CMD [ "fastapi", "dev", "./main.py", "--host=0.0.0.0" ]
