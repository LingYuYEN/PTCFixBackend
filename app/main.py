import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.create import create_router
from routes.read import read_router
from routes.update import update_router
# from config.ssl import generate_certificate
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
    allow_headers=["*"],
)

app.include_router(read_router, tags=['GET'])
app.include_router(create_router, tags=['POST'])
app.include_router(update_router, tags=['PUT'])

# generate_certificate()

if __name__ == '__main__':
    # uvicorn.run('main:app', host="127.0.0.1", port=5000, log_level="info", reload=True, ssl_keyfile="./key.pem", ssl_certfile="./cert.pem", workers=1)
    uvicorn.run('main:app', host="127.0.0.1", port=5000, log_level="info", reload=True, workers=1)
