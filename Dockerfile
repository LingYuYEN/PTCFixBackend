FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
#複製 requirements.txt進入 docker 內部
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY ./app /app