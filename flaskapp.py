from flask import Flask,request

app = Flask(__name__)
app.secret_key = "Secret Key"