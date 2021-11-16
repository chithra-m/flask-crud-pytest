from flaskapp import app,request
from crud import read_all , update_task , create_task , delete_task

@app.route('/')
def index():
    return read_all()

@app.route('/insert', methods = ['POST'])
def insert () :
    return create_task()

@app.route('/update', methods = ['GET', 'POST'])
def update():
    return update_task()

@app.route('/delete/<taskid>/', methods = ['GET', 'POST'])
def delete(taskid):
    return delete_task(taskid)

if __name__ == "__main__":
    app.run(debug=True)