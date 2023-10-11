import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from routes import read, create, update
# from config.ssl import generate_certificate
from config.db import db
from models.model import Signin

app = FastAPI()

app.debug = True

origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    # HTTPSRedirectMiddleware,
    # TrustedHostMiddleware,
    # allowed_hosts=["*.swellrshsps.tk"],
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# app.include_router(read.read_router, tags=['GET'])
# app.include_router(create.create_router, tags=['POST'])
# app.include_router(update.update_router, tags=['PUT'])

# generate_certificate()


@app.post("/signin")
async def create_signin(signin: Signin):
    collection = db['members']
    myquery = {'account': signin.account}
    # myquery = {'account': 'yuxp0130@gmail.com'}
    myCol = collection.find_one(myquery, {'_id': 0})
    result = False if myCol is None else True
    print(result)
    return {"status": "Ok", "data": result}

if __name__ == '__main__':
    # uvicorn.run('main:app', host="0.0.0.0", port=5000, log_level="info", reload=True, ssl_keyfile="./key.pem", ssl_certfile="./cert.pem", workers=1)
    uvicorn.run('main:app', host="127.0.0.1", port=5000, log_level="info", reload=True, workers=1)
