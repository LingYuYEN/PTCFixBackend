import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import read, create, update
from config.ssl import generate_certificate

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

# app.add_middleware(
#     HTTPSRedirectMiddleware
# )


# @app.route("/")
# async def index():
#     return JSONResponse({"message": "success"}, status_code=200)
#
#
# @app.route("/", methods=['OPTIONS'])
# async def options():
#     return JSONResponse(
#         {},
#         headers={
#             'Allow': 'GET, POST, OPTIONS',
#             'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
#             'Access-Control-Allow-Origin': '*',
#             'Access-Control-Allow-Headers': '*'
#         }
#     )

app.include_router(read.read_router, tags=['GET'])
app.include_router(create.create_router, tags=['POST'])
app.include_router(update.update_router, tags=['PUT'])

generate_certificate()


if __name__ == '__main__':
    # uvicorn.run('main:app', host="0.0.0.0", port=5000, log_level="info", reload=True, ssl_keyfile="./key.pem", ssl_certfile="./cert.pem", workers=1)
    uvicorn.run('main:app', host="127.0.0.1", port=5000, log_level="info", reload=True, workers=1)
