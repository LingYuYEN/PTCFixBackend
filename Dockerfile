FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./cert.pem ./cert.pem
COPY ./key.pem ./key.pem
EXPOSE 443
#複製 requirements.txt進入 docker 內部
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./app /app