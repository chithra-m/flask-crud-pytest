from db import db

class Tasks(db.Model):
    __tablename__ = 'tasks'
    taskid = db.Column(db.Integer , primary_key = True)
    taskname = db.Column(db.String(100) )
    status = db.Column(db.String(100))
    enddate = db.Column(db.String(100))

    def __init__(self, taskid,taskname, status, enddate):
        self.taskid = taskid
        self.taskname = taskname
        self.status = status
        self.enddate = enddate