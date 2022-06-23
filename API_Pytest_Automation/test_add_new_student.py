import requests
import json
import jsonpath
import pytest

@pytest.fixture(scope = "module")
def fixture_code():
    print("------------------------------------------")
    print("This is Starting of Code")
    print("------------------------------------------")
    yield
    print("------------------------------------------")
    print("This is End of Code")
    print("------------------------------------------")

def test_add_student_data(fixture_code):
    API_url = "https://reqres.in/api/users"
    Request_file = "C://Users//shaz5//Desktop//Learn//APITesting//PytestLearning//Files//pytest_Api_Cretae_Student.json"
    Requestobj = open(Request_file,"r")
    jsonrequest = json.loads(Requestobj.read())
    print(jsonrequest)
    Response = requests.post(API_url,jsonrequest)
    print(Response.text)
    jsonresponse = json.loads(Response.text)
    name = jsonpath.jsonpath(jsonresponse,"name")
    assert Response.status_code == 201
    assert name[0] == 'morpheus'

def test_get_student_data(fixture_code):
    global id
    global First_Name
    API_url = "https://reqres.in/api/users/3"
    Response = requests.get(API_url)
    print(Response.text)
    jsonresponse = json.loads(Response.text)
    First_Name = jsonpath.jsonpath(jsonresponse,"data.first_name")
    id = jsonpath.jsonpath(jsonresponse,"data.id")
    print(First_Name)
    assert Response.status_code == 200


def test_update_student_data(fixture_code):
    API_url = "https://reqres.in/api/users/2"
    Request_file = "C://Users//shaz5//Desktop//Learn//APITesting//PytestLearning//Files//pytest_Api_update_Student.json"
    Requestobj = open(Request_file,"r")
    jsonrequest = json.loads(Requestobj.read())
    print(jsonrequest)
    jsonrequest["name"] = First_Name[0]
    print(jsonrequest)
    Response = requests.put(API_url,jsonrequest)
    print(Response.text)
    jsonresponse = json.loads(Response.text)
    name = jsonpath.jsonpath(jsonresponse,"name")
    assert Response.status_code == 200
    print(name)
    assert name[0] == name[0]


def test_delete_student_data(fixture_code):
    API_url = "https://reqres.in/api/users/"+str(id[0])
    Response = requests.delete(API_url)
    print(Response.text)
    assert Response.status_code == 204
