from flask import Flask, render_template
import json
from github import Github
from github import Auth
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
envfile = open("backend/env.json","r")
envcontent = json.loads(envfile.read())
auth = Auth.Token(envcontent["getghtoken"])
gh = Github(auth=auth)

class repodata():
    def __init__(self,name,description,lic,owner,url,lang):
        self.name = name
        self.description = description
        self.lic = lic
        self.owner = owner
        self.url = url
        self.lang = lang
def getrepos():
    repolist = []
    for repo in gh.get_user().get_repos():
        if repo.visibility == "public":
            name = repo.name
            description = repo.description
            if not repo.license == None:
                lic = str(repo.license)[14:-2]
            else:
                lic = "Unspecified License"
            owner = str(repo.owner)[17:-2]
            url = f"https://github.com/{owner}/{name}"
            lang = repo.language
            repolist.append(repodata(name,description,lic,owner,url,lang))
        else:
            continue
    return repolist
@app.route('/getgithub',methods=['GET'])
def getgithub():
    repos = getrepos()
    repols = []
    for i in repos:
        rdict = {
            "name": i.name,
            "description": i.description,
            "lic": i.lic,
            "owner": i.owner,
            "url": i.url,
            "lang": i.lang
        }
        repols.append(rdict)
    repojson = json.dumps(repols)
    return repojson
if __name__ == '__main__':
    app.run(debug=True)