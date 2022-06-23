import requests
import json
import jsonpath
import pytest
import openpyxl
from Data_Driven_Testing import Library

def test_login():
    #API
    API_url = "https://reqres.in/api/login"
    Request_file = "C://Users//shaz5//Desktop//Learn//APITesting//PytestLearning//Files//Login.json"
    Requestobj = open(Request_file, "r")
    jsonrequest = json.loads(Requestobj.read())

    obj = Library.Common('C://Users//shaz5//Desktop//Learn//APITesting//PytestLearning//Files//loginopenpyxl.xlsx',"Sheet1")
    col_count = obj.fetch_column_count()
    row_count = obj.fetch_row_count()
    ColumnList = obj.fetch_Column_name()

    for i in range(2,row_count+1):
        updated_jsonrequest = obj.update_Request_with_data(i,jsonrequest,ColumnList)
        Response = requests.post(API_url, updated_jsonrequest)
        print(Response.text)
        print(Response.status_code)

        #cell_email = sh.cell(row=i,column=1)
        #cell_password = sh.cell(row=i,column=2)
        #jsonrequest['email'] = cell_email.value
        #jsonrequest['password'] = cell_password.value
        #print(jsonrequest)
        #Response = requests.post(API_url, jsonrequest)
        #print(Response.text)
        #print(Response.status_code)
    #jsonresponse = json.loads(Response.text)
    #First_Name = jsonpath.jsonpath(jsonresponse,"data.first_name")
    #id = jsonpath.jsonpath(jsonresponse,"data.id")
    #print(First_Name)
    #assert Response.status_code == 200