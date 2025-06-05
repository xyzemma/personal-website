class repobox {
    constructor(name,description,lic,owner,url,lang) {
        this.name = name;
        this.description = description;
        this.lic = lic;
        this.owner = owner;
        this.url = url;
        this.lang = lang;
        this.titlefield = document.createElement("h2");
        this.titlelink = document.createElement("a");
        this.descfield = document.createElement("p");
        this.licfield = document.createElement("p");
        this.langfield = document.createElement("p");
        this.titlelink.href = this.url;
        this.titlelink.innerText = this.name;
        this.descfield.innerText = this.description;
        this.licfield.innerText = this.lic;
        this.langfield.innerText = this.lang;
        this.titlefield.appendChild(this.titlelink);
        document.body.appendChild(this.titlefield);
        document.body.appendChild(this.descfield);
        document.body.appendChild(this.licfield);
        document.body.appendChild(this.langfield);
        


    }
}
async function fetchAsync (url) {
    let response = await fetch(url);
    let data = await response.json();
    return data;
  }
async function main() {
    var ghjson = await fetchAsync("http://localhost:5000/getgithub");
    var repoboxls = []
    console.log(ghjson);
    console.log(ghjson.length);
    for (let i = 0;i<ghjson.length;i++){
        var repo = ghjson[i];
        console.log(repo);
        console.log(repo["name"]);
        repoboxls.push(new repobox(repo["name"],repo["description"],repo["lic"],repo["owner"],repo["url"],repo["lang"]))

    }
}
main()