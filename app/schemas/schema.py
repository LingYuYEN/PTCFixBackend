from datetime import datetime, timedelta
from chinese_calendar import is_workday


def data_serializer(data) -> dict:
    # data['_id']
    dataDict = dict(data)
    return dataDict


def data_list_serializer(dataList) -> list:
    return [data_serializer(data) for data in dataList]


def fixInfo_serializer(fixInfo) -> dict:
    return {
        'department': fixInfo['department'],
        'office': fixInfo['office'],
        'name': fixInfo['name'],
        'tel': fixInfo['tel'],
        'type': fixInfo['type'],
        'description': fixInfo['description'],
        'start_time': fixInfo['start_time'],
        'status': fixInfo['status'],
        'score': fixInfo['score'],
        'isScore': fixInfo['isScore'],
    }


def fixInfos_serializer(fixInfos) -> list:
    return [fixInfo_serializer(fixInfo) for fixInfo in fixInfos]


def fixDetail_serializer(fixDetail) -> dict:
    return {
        'time': fixDetail['time'],
        'info': fixDetail['info'],
        'user': fixDetail['user']
    }


def fixDetails_serializer(fixDetails) -> list:
    return [fixDetail_serializer(fixDetail) for fixDetail in fixDetails]


def work_times(start_time_str, end_time_str):
    start_time = datetime.strptime(start_time_str, '%Y/%m/%d %H:%M:%S')
    end_time = datetime.strptime(end_time_str, '%Y/%m/%d %H:%M:%S')

    work_hours = timedelta(hours=0)

    while start_time < end_time:
        if is_workday(start_time.date()):
            work_hours += timedelta(hours=0.5)
        start_time += timedelta(hours=0.5)

    return work_hours
