FROM tiangolo/uvicorn-gunicorn:python3.10
#FROM python:3.10

# 安装 FastAPI 和 Uvicorn
#RUN pip install fastapi uvicorn

# Copy your FastAPI code to the image
COPY . /app

# Set the working directory
WORKDIR /app

RUN pip install --upgrade pip

#複製 requirements.txt進入 docker 內部
COPY ./requirements.txt requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

#RUN apt-get update

#RUN apt-get install vim -y

# 安装 OpenSSL
RUN apt-get update && apt-get install -y openssl

# 生成自签名的证书和私钥
RUN openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365

# 将证书和私钥复制到镜像中
COPY cert.pem /app/cert.pem
COPY key.pem /app/key.pem

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload", "--port", "5000"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000", "--ssl-keyfile", "/app/key.pem", "--ssl-certfile", "/app/cert.pem"]
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0" , "--reload" , "--port", "5000", "--ssl-keyfile", "/app/key.pem", "--ssl-certfile", "/app/cert.pem"]