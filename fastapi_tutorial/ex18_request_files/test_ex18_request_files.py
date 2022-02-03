from fastapi import status
from fastapi.testclient import TestClient
from fastapi_tutorial.ex18_request_files.main import app
import os



client = TestClient(app)

def test_files():

    folder = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(folder, "test.dat")
    file_size = os.path.getsize(filename)

    files_data = {
        "file": ("test.dat", open(filename, "rb"), "text/plain")
    }

    response_data = {
        "file_size": file_size
    }

    response = client.post(f"/files/", files=files_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == response_data

def test_uploadfile():

    folder = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(folder, "test.dat")
    file_size = os.path.getsize(filename)

    files_data = {
        "file": ("test.dat", open(filename, "rb"), "text/plain")
    }

    response_data = {
        "filename": "test.dat",
        "content_type": "text/plain",
        "_in_memory": True
    }

    response = client.post(f"/uploadfile/", files=files_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == response_data




def test_files_many():

    folder = os.path.dirname(os.path.abspath(__file__))

    filename1 = "test.dat"
    fullfilename1 = os.path.join(folder, filename1)
    file_size1 = os.path.getsize(fullfilename1)
    file_type1 = "text/plain"

    filename2 = "moons.csv"
    fullfilename2 = os.path.join(folder, filename2)
    file_size2 = os.path.getsize(fullfilename2)
    file_type2 = "text/plain"

    filename3 = "PIA09258_callisto.jpg"
    fullfilename3 = os.path.join(folder, filename3)
    file_size3 = os.path.getsize(fullfilename3)
    file_type3 = "image/jpeg"

    files_data = (
        ("files", (filename1, open(fullfilename1, "rb"), file_type1)),
        ("files", (filename2, open(fullfilename2, "rb"), file_type2)),
        ("files", (filename3, open(fullfilename3, "rb"), file_type3))
    )

    response_data = {
        "file_sizes": [file_size1, file_size2, file_size3]
    }


    response = client.post(f"/files/many/", files=files_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == response_data

def test_uploadfile_many():

    folder = os.path.dirname(os.path.abspath(__file__))

    filename1 = "test.dat"
    fullfilename1 = os.path.join(folder, filename1)
    file_type1 = "text/plain"

    filename2 = "moons.csv"
    fullfilename2 = os.path.join(folder, filename2)
    file_type2 = "text/plain"

    filename3 = "PIA09258_callisto.jpg"
    fullfilename3 = os.path.join(folder, filename3)
    file_type3 = "image/jpeg"

    files_data = (
        ("files", (filename1, open(fullfilename1, "rb"), file_type1)),
        ("files", (filename2, open(fullfilename2, "rb"), file_type2)),
        ("files", (filename3, open(fullfilename3, "rb"), file_type3))
    )

    response_data = {
        "filenames": [filename1, filename2, filename3]
    }

    response = client.post(f"/uploadfiles/many/", files=files_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == response_data