#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
FROM tiangolo/uvicorn-gunicorn:python3.10

#複製 requirements.txt進入 docker 內部
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN pip install pyOpenSSL

#RUN sudo apt-get update
#RUN sudo apt-get install nginx
#FROM nginx
# Remove the default nginx.conf
#RUN rm /etc/nginx/conf.d/default.conf

# Replace with our own nginx.conf
#COPY nginx.conf /etc/nginx/conf.d/
#
#COPY ./app/cert.pem /etc/nginx/ssl.csr
#COPY ./app/key.pem /etc/nginx/ssl.key
#COPY ./app/cert.pem /cert.pem
#COPY ./app/key.pem /key.pem
#
#EXPOSE 443

COPY ./app /app

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
CMD ["uvicorn", "main:app", "--host=127.0.0.1" , "--reload" , "--port", "5000"]