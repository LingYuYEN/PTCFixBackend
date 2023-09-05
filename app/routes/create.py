from fastapi import APIRouter
from schemas.schema import data_list_serializer
from config.db import db
# from config.db import collection
from models.model import FixInfo, Member, Signin

create_router = APIRouter()


@create_router.post("/signin")
async def create_signin(signin: Signin):
    collection = db['members']
    myquery = {'account': signin.account}
    myCol = collection.find(myquery, {'_id': 0})
    result = False if myCol.count() == 0 else True
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
