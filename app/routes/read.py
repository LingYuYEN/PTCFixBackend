from fastapi import APIRouter
from schemas.schema import data_list_serializer
from config.db import db
# from config.db import collection

read_router = APIRouter()


@read_router.get("/all_id")
async def get_all_ids():
    collection = db['fixInfos']
    myCol = collection.find({}, {'_id': 0})
    # for col in myCol:
    #     print(col.get('_id'))
    ids = data_list_serializer(myCol)
    return {"status": "Ok", "data": ids}


@read_router.get("/all_members")
async def get_all_members():
    collection = db['members']
    myCol = collection.find({}, {'_id': 0})
    members = data_list_serializer(myCol)
    return {"status": "Ok", "data": members}


@read_router.get("/get_member_by_account")
async def get_members_by_account(account):
    collection = db['members']
    myCol = collection.find({'account': account}, {'_id': 0})
    members = data_list_serializer(myCol)
    return {"status": "Ok", "data": members}


@read_router.get("/all_departments")
async def get_all_members():
    collection = db['department']
    myCol = collection.find({}, {'_id': 0})
    departments = data_list_serializer(myCol)
    return {"status": "Ok", "data": departments}


@read_router.get("/all_fixInfos")
async def get_all_fixInfos():
    collection = db['fixInfos']
    myColList = collection.find({}, {'_id': 1})
    myColIdList = []
    for myColId in myColList:
        myColIdList.append(str(myColId['_id']))

    myCol = collection.find({}, {'_id': 0})
    fixInfos = data_list_serializer(myCol)
    return {"status": "Ok", '_id': myColIdList, "data": fixInfos}


@read_router.get("/get_fixInfos_by_account")
async def get_fixInfos_by_account(account):
    collection = db['fixInfos']

    myColList = collection.find({'account': account}, {'_id': 1})
    myColIdList = []
    for myColId in myColList:
        myColIdList.append(str(myColId['_id']))

    myCol = collection.find({'account': account}, {'_id': 0})
    fixInfos = data_list_serializer(myCol)
    return {"status": "Ok", '_id': myColIdList, "data": fixInfos}
