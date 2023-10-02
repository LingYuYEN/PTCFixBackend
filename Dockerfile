#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /code

#複製 requirements.txt進入 docker 內部
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
#COPY ./cert.pem /cert.pem
#COPY ./key.pem /key.pem

COPY ./app /code/app

EXPOSE 80
CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "9000"]
#CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "9000"]
#CMD ["uvicorn", "main:app", "--host=127.0.0.1" , "--reload" , "--port", "9000"]