from db import db
from model import Tasks
import json


def gettaskall():
    try:       
        task_results =  Tasks.query.all()
        res = {}
        for task in task_results:
            temp = {}
            temp = {
                'taskid' : task.taskid,
                'taskname': task.taskname,
                'status': task.status,
                'enddate': task.enddate 
            }
            #temp['taskname'],temp['status'],temp['enddate'] = task.taskname,task.status, task.enddate
            res[task.taskid] = temp
            
        return res
    except Exception as error:
        return str(error)

def gettaskid(taskid): 
    try:       
        task_results= Tasks.query.filter_by(taskid = taskid)
        #task_results = [Tasks(taskid=20,taskname="task20",status="completed",enddate="901234")]
        res = {}
        for task in task_results:
            temp = {}
            temp = {
                'taskid' : task.taskid,
                'taskname': task.taskname,
                'status': task.status,
                'enddate': task.enddate 
            }
            #temp['taskname'],temp['status'],temp['enddate'] = task.taskname,task.status, task.enddate
            res[task.taskid] = temp
            
        return res
    except Exception as error:
        return str(error)


def posttask(data):
    try:
        data = json.loads(data)
        if isinstance(data,dict):
            data = [data]
        for task in data:
            my_data = Tasks(taskid = task['taskid'], taskname = task['taskname'], status = task['status'], enddate = task['enddate'])
            db.session.add(my_data)
        db.session.commit()
        return "Inserted Successfully"
    except Exception as error:
        return "error occurred"
  

def puttask(data):
    try:
        data = json.loads(data)
        if isinstance(data,dict):
            data = [data]
        for task in data:
            updatetask = Tasks.query.get(task['taskid'])
            if updatetask.taskid :
                updatetask.taskname = task['taskname']
                updatetask.status = task['status']
                updatetask.enddate = task['enddate']
            
                db.session.commit()
                return "Updated Successfully"
    except Exception as error:
        return "error occurred"
      

def deletetask(taskid):
    try:
        if taskid:
            db.session.delete(Tasks.query.get(taskid))
            db.session.commit()
        return "Deleted Successfully"
    except Exception as error:
        return "error occurred"