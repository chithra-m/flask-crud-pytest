from db import db
from model import Tasks
from flaskapp import app,request
from flask import render_template,redirect,url_for,request

def read_all():
    all_data = db.session.query(Tasks)
    #all_data = Tasks.query.all()
    return render_template("index.html", tasklists = all_data)

def create_task():
    if request.method == 'POST':
        taskid = request.form['taskid']
        taskname = request.form['taskname']
        status = request.form['status']
        enddate = request.form['enddate']
        my_data = Tasks(taskid,taskname, status, enddate)
        db.session.add(my_data)
        db.session.commit()
    return redirect(url_for('index'))

def update_task():

    if request.method == 'POST':
        my_data = Tasks.query.get(request.form.get('taskid'))

        my_data.taskname = request.form['taskname']
        my_data.status = request.form['status']
        my_data.enddate = request.form['enddate']

        db.session.commit()
        return redirect(url_for('index'))

def delete_task(taskid):
    my_data = Tasks.query.get(taskid)
    db.session.delete(my_data)
    db.session.commit()

    return redirect(url_for('index'))