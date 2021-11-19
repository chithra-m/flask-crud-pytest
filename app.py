from flaskapp import app,request
from services import gettaskall,gettaskid,posttask,puttask,deletetask
from model import Tasks

@app.route('/task',methods=['GET'])
def read_task_all():
    return gettaskall()

@app.route('/task/<taskid>',methods=['GET'])
def read_task_id(taskid):
   return gettaskid(taskid)

@app.route('/task',methods=['POST'])
def insert_task():
    return posttask(request.data)

@app.route('/task',methods=['PUT'])
def update_task():
    return puttask(request.data)

@app.route('/task/<taskid>',methods=['DELETE'])
def delete_task(taskid):
    return deletetask(taskid)

if __name__ == "__main__":
    app.run(debug=True)