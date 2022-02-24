from fastapi.testclient import TestClient
import sys        
sys.path.insert(0, '../Lab05')        
from main import app

client = TestClient(app)

def test_call_test_api():
    response = client.get("/courses/test")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_call_post_api():
    response = client.post("/courses/post")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_call_post_data_api():
    input = "prateep"
    response = client.post("/courses/body",
        json = {"name": input}    
    )
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello "+input}

# def test_post_insert():
#     response = client.post(
#         "/students/",
#         json={
#             "name": "string",
#             "description": "string",
#             "completed": "true",
#             "date": "string"
#         }
#     )
#     assert response.status_code == 200
#     assert response.json()[0]["name"] == "string"