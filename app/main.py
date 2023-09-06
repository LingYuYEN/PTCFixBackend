import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.create import create_router
from app.routes.read import read_router
from app.routes.update import update_router


fastapi = FastAPI()

fastapi.debug = True
origins = [
    "*"
]

fastapi.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fastapi.include_router(read_router, tags=['GET'])
fastapi.include_router(create_router, tags=['POST'])
fastapi.include_router(update_router, tags=['PUT'])

if __name__ == '__main__':

    uvicorn.run('app.main:fastapi', host="127.0.0.1", port=5000, log_level="info", reload=True, workers=1)
