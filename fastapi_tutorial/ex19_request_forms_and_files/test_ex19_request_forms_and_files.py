from fastapi import status
from fastapi.testclient import TestClient
from fastapi_tutorial.ex19_request_forms_and_files.main import app
import os

client = TestClient(app)

def test_files():

    folder = os.path.dirname(os.path.abspath(__file__))

    filename1 = "moons.csv"
    fullfilename1 = os.path.join(folder, filename1)
    file_size1 = os.path.getsize(fullfilename1)

    filename2 = "PIA09258_callisto.jpg"
    fullfilename2 = os.path.join(folder, filename2)
    file_size2 = os.path.getsize(fullfilename2)

    files_data = {
        "file": (filename1, open(fullfilename1, "rb"), "text/plain"),
        "fileb": (filename2, open(fullfilename2, "rb"), "image/jpeg")
    }

    response_data = {
        "file_size": file_size1,
        "token": "foo",
        "fileb_content_type": "image/jpeg",
    }

    response = client.post(f"/files/",
        files=files_data,
        data={"token": "foo"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == response_data