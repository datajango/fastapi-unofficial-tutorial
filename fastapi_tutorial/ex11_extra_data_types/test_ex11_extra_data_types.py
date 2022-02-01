from fastapi.testclient import TestClient
from fastapi_tutorial.ex11_extra_data_types.main import app
from unittest import TestCase
from datetime import datetime, time, timedelta, timezone, tzinfo
from zoneinfo import ZoneInfo
import json
from uuid import UUID
import uuid

client = TestClient(app)

def test_items_01():

    item_id = str(uuid.uuid1())
    start_datetime = datetime(2022,1,2,0,0,0,0,None)
    end_datetime = datetime(2022,2,2,0,0,0,0,None)
    repeat_at = time(11,0,0)
    process_after = timedelta(days=3)

    start_process =  start_datetime + process_after
    duration = end_datetime - start_process

    request_data = {
        "start_datetime": str(start_datetime.strftime("%Y-%m-%dT%H:%M:%S+00:00")),
        "end_datetime": str(end_datetime.strftime("%Y-%m-%dT%H:%M:%S+00:00")),
        "repeat_at": repeat_at.strftime("%H:%M:%S"),
        "process_after": process_after.total_seconds()
    }

    response_data = {
        "item_id": item_id,
        "start_datetime": str(start_datetime.strftime("%Y-%m-%dT%H:%M:%S+00:00")),
        "end_datetime": str(end_datetime.strftime("%Y-%m-%dT%H:%M:%S+00:00")),
        "repeat_at": repeat_at.strftime("%H:%M:%S"),
        "process_after": process_after.total_seconds(),
        "start_process": str(start_process.strftime("%Y-%m-%dT%H:%M:%S+00:00")),
        "duration": duration.total_seconds(),
    }

    response = client.put(f"/items/{item_id}", json=request_data)
    assert response.status_code == 200
    assert response.json() == response_data
