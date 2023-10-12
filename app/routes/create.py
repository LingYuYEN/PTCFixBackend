from fastapi import APIRouter
from app.schemas.schema import data_list_serializer
from app.config.db import db
from app.models.model import FixInfo, Member, Signin

create_router = APIRouter()


@create_router.post("/signin")
async def create_signin(signin: Signin):
    collection = db['members']
    myquery = {'account': signin.account}
    # myquery = {'account': 'yuxp0130@gmail.com'}
    myCol = collection.find_one(myquery, {'_id': 0})
    result = False if myCol is None else True
    print(result)
    return {"status": "Ok", "data": result}


@create_router.post("/create_member")
async def create_member(member: Member):
    collection = db['members']
    _id = collection.insert_one(dict(member)).inserted_id
    member = data_list_serializer(collection.find({"_id": _id}, {'_id': 0}))
    return {"status": "Ok", "data": member}


@create_router.post("/create_fix")
async def create_fix(fixInfo: FixInfo):
    collection = db['fixInfos']
    _id = collection.insert_one(dict(fixInfo)).inserted_id
    fixInfo = data_list_serializer(collection.find({"_id": _id}, {'_id': 0}))
    return {"status": "Ok", "data": fixInfo}
