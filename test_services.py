import pytest
import json
from services import gettaskall,gettaskid, posttask, puttask, deletetask
from model import Tasks


def convert_faketask(fake_Tasks):        
    res = {}
    for task in fake_Tasks:
        temp = {}
        temp = {
            'taskid' : task.taskid,
            'taskname': task.taskname,
            'status': task.status,
            'enddate': task.enddate           
        }
        res[task.taskid] =  temp
    return res


def test_gettaskAll(mocker):
    fake_Tasks = [Tasks(taskid=20,taskname="task20",status="completed",enddate="901234"), Tasks(taskid=22,taskname="task22",status="completed",enddate="901234")]    
    mocker.patch('services.gettaskall', return_value = fake_Tasks)     
    response1 = gettaskall()
    fake_response1 = convert_faketask(fake_Tasks)  
    print('fake ' ,response1)
    print('thrtj',fake_response1)
    assert response1 == fake_response1    
    
    
def test_gettaskId(mocker):    
    fake_Tasks = [Tasks(taskid=20,taskname="task20",status="completed",enddate="901234")]
    mocker.patch('services.gettaskid',return_value = fake_Tasks)    
    response = gettaskid(20)
    fake_response = convert_faketask(fake_Tasks)
    print('fake',response)
    print('thrtj',fake_response)
    assert response == fake_response
    

def test_posttaskp(mocker):
    mocker.patch('services.posttask', return_value = "Inserted Successfully")
    fake_data = json.dumps({"taskid" : 5, "taskname" : "task1" , "status" : "completed", "enddate":"901234"})
    response = posttask(fake_data)    
    assert response == "Inserted Successfully"


def test_posttaskn(mocker):
    fake_data = json.dumps({"taskname":"task1","status": "completed"})
    response = posttask(fake_data)
    assert "error occurred" in response
    
    
def test_puttaskp(mocker):
    mocker.patch('services.puttask', return_value = "Updated Successfully")
    fake_data = json.dumps({"taskid" : 10 ,"taskname" : "task10" , "status" : "completed" , "enddate" : "901234"})
    response = puttask(fake_data)   
    assert response == "Updated Successfully"

 
def test_puttaskn(mocker):
    fake_data = json.dumps({"taskid" : 123 , "taskname" : "task" , "status" : "in-progress" , "enddate" : "901234"})
    response = puttask(fake_data)    
    assert "error occurred" in response


def test_deletetaskp(mocker):
    mocker.patch('services.deletetask', return_value = "Deleted Successfully")
    response = deletetask(1)    
    assert response == "Deleted Successfully"


def test_deletetaskn(mocker):
    response = deletetask('8')    
    assert "error occurred" in response