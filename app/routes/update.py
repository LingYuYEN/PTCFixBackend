from fastapi import APIRouter
from app.schemas.schema import data_list_serializer, work_times
from app.config.db import db
from app.models.model import FixDetail, ModifyEngneer, FixUpdate, ModifyVisit
from bson.objectid import ObjectId

update_router = APIRouter()


@update_router.put("/update_fix")
async def update_fix(fixUpdate: FixUpdate):
    collection = db['fixInfos']
    objInstance = ObjectId(fixUpdate.objectId)

    myQuery = {'_id': objInstance}
    newValues = {'$set': {
        'department': fixUpdate.department,
        'office': fixUpdate.office,
        'engneer': fixUpdate.engneer,
        'type': fixUpdate.type,
        'description': fixUpdate.description,
        'reason': fixUpdate.reason,
        'replaceComponent': fixUpdate.replaceComponent,
        'status': fixUpdate.status,
        'isScore': fixUpdate.isScore,
        'end_time': fixUpdate.end_time
    }}
    collection.update_one(myQuery, newValues)

    start_time_db = collection.find_one({"_id": objInstance}, {'start_time': 1})
    if fixUpdate.end_time != '':
        diff_time = work_times(start_time_db['start_time'], fixUpdate.end_time)
        collection.update_one(myQuery, {'$set': {
            'diff_time': str(diff_time),
        }})
    else:
        collection.update_one(myQuery, {'$set': {
            'diff_time': '',
        }})

    responseData = data_list_serializer(collection.find({"_id": objInstance}, {'_id': 0}))
    return {"status": "Ok", "data": responseData}


@update_router.put("/update_detail")
async def update_detail(fixDetail: FixDetail):
    collection = db['fixInfos']
    objInstance = ObjectId(fixDetail.objectId)
    myQuery = {'_id': objInstance}
    newValues = {'$push': {'fixDetails': {
        'user': fixDetail.user,
        'info': fixDetail.info,
        'time': fixDetail.time,
        'msgPriority': fixDetail.msgPriority
    }}}
    collection.update_one(myQuery, newValues)

    fixDetails = data_list_serializer(collection.find({"_id": objInstance}, {'_id': 0}))
    return {"status": "Ok", "data": fixDetails}


@update_router.put("/update_engneer")
async def update_engneer(modifyEngneer: ModifyEngneer):
    collection = db['fixInfos']
    objInstance = ObjectId(modifyEngneer.objectId)
    myQuery = {'_id': objInstance}
    newValues = {'$set': {
        'engneer': modifyEngneer.engneer,
        'status': '處理中'
    }}
    collection.update_one(myQuery, newValues)
    engneer = data_list_serializer(collection.find({"_id": objInstance}, {'_id': 0}))
    return {"status": "Ok", "data": engneer}


@update_router.put("/update_visit")
async def update_visit(modifyVisit: ModifyVisit):
    collection = db['fixInfos']
    objInstance = ObjectId(modifyVisit.objectId)
    myQuery = {'_id': objInstance}
    newValues = {'$set': {
        'score': modifyVisit.score,
        'isScore': True,
        'status': '結案'
    }}
    collection.update_one(myQuery, newValues)
    data = data_list_serializer(collection.find({"_id": objInstance}, {'_id': 0}))
    return {"status": "Ok", "data": data}
