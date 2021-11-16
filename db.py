from flask_sqlalchemy import SQLAlchemy
from flaskapp import app
from settings import user,passwd,db,host

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{passwd}@{host}/{db}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)