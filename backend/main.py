from flask import Flask
import json
from github import Github

app = Flask(__name__)
envcontent = json.loads("env.json")

@app.route('/getgithub')
def getgithub():
