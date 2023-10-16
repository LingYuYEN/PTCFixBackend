import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import read, create, update
# from config.ssl import generate_certificate
# from config.db import db
# from models.model import Signin

app = FastAPI()

app.debug = True

origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# @app.get('/')
# def index():
#     return {'title': 'hello'}
app.include_router(read.read_router, tags=['GET'])
app.include_router(create.create_router, tags=['POST'])
app.include_router(update.update_router, tags=['PUT'])

# generate_certificate()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
    # uvicorn.run('main:app', host="0.0.0.0", port=5000, log_level="info", reload=True, ssl_keyfile="./key.pem", ssl_certfile="./cert.pem", workers=1)
    # uvicorn.run('main:app', host="0.0.0.0", port=5000, log_level="info", reload=True, workers=1)
