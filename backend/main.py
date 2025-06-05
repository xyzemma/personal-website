from flask import Flask, render_template
import json
from github import Github
from github import Auth
from flask_cors import CORS
from bs4 import BeautifulSoup
import urllib.request
import webbrowser


app = Flask(__name__)
CORS(app)
envfile = open("backend/env.json","r")
envcontent = json.loads(envfile.read())
auth = Auth.Token(envcontent["getghtoken"])
gh = Github(auth=auth)

def get_pfp(user):
    profileurl = f"https://github.com/{user}"
    profilehtml = urllib.request.urlopen(profileurl).read()
    profilesoup = BeautifulSoup(profilehtml)
    pfptag = profilesoup.find('img',{"class":"avatar"})
    pfpurl = pfptag["src"]
    return pfpurl


class repodata():
    def __init__(self,name,description,lic,owner,url,lang,pfp):
        self.name = name
        self.description = description
        self.lic = lic
        self.owner = owner
        self.url = url
        self.lang = lang
        self.pfp = pfp
def getrepos():
    repolist = []
    for repo in gh.get_user().get_repos():
        if repo.visibility == "public":
            name = repo.name
            if not repo.description == None:
                description = repo.description
            else:
                description = "No Description Provided"
            if not repo.license == None:
                lic = str(repo.license)[14:-2]
            else:
                lic = "Unspecified License"
            owner = str(repo.owner)[17:-2]
            pfp = get_pfp(owner)
            url = f"https://github.com/{owner}/{name}"
            if not repo.language == None:
                lang = repo.language
            else:
                lang = "No language detected"
            repolist.append(repodata(name,description,lic,owner,url,lang,pfp))
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
            "lang": i.lang,
            "pfp": i.pfp
        }
        repols.append(rdict)
    repojson = json.dumps(repols)
    return repojson
if __name__ == '__main__':
    app.run(debug=True)