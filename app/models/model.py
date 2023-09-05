from pydantic import BaseModel
from typing import List


class Signin(BaseModel):
    account: str


class Member(BaseModel):
    account: str
    name: str
    tel: str
    department: str
    office: str
    priority: int = 1


class FixUpdate(BaseModel):
    objectId: str
    department: str
    office: str
    engneer: str
    type: str
    description: str
    reason: str
    replaceComponent: str
    status: str
    isScore: bool = False
    end_time: str = ''


class FixDetail(BaseModel):
    objectId: str
    user: str
    info: str
    time: str
    msgPriority: int


class FixInfo(BaseModel):
    account: str
    name: str
    tel: str
    department: str
    office: str
    engneer: str
    type: str
    description: str
    start_time: str
    end_time: str = ''
    status: str = '未接案'
    score: int = 0
    isScore: bool = False
    fixMsgs: List[FixDetail] = []


class ModifyEngneer(BaseModel):
    objectId: str
    engneer: str


class ModifyVisit(BaseModel):
    objectId: str
    score: int
