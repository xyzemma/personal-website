class repobox {
    constructor(name,description,lic,owner,url,lang,pfp) {
        this.name = name;
        this.description = description;
        this.lic = lic;
        this.owner = owner;
        this.url = url;
        this.lang = lang;
        this.pfp = pfp;
        this.container = document.createElement("div");
        this.container.className = "repobox"
        this.textdiv = document.createElement("div");
        this.textdiv.className = "rbtextdiv"
        this.titlefield = document.createElement("h2");
        this.titlefield.className = "rbtext"
        this.titlelink = document.createElement("a");
        this.titlelink.className = "rblink"
        this.descfield = document.createElement("p");
        this.descfield.className = "rbtext"
        this.licfield = document.createElement("p");
        this.licfield.className = "rbtext"
        this.langfield = document.createElement("p");
        this.langfield.className = "rbtext";
        this.pfptag = document.createElement("img");
        this.pfptag.className = "rbpfp";
        this.titlelink.href = this.url;
        this.titlelink.innerText = this.name;
        this.descfield.innerText = "📁 | " + this.description;
        this.licfield.innerText = "⚖ | "+this.lic;
        this.langfield.innerText = "📜 | " +this.lang;
        this.pfptag.src = this.pfp;
        this.titlefield.appendChild(this.titlelink);
        this.textdiv.appendChild(this.titlefield);
        this.textdiv.appendChild(this.descfield);
        this.textdiv.appendChild(this.licfield);
        this.textdiv.appendChild(this.langfield);
        this.container.appendChild(this.textdiv);
        this.container.appendChild(this.pfptag);
        document.body.appendChild(this.container);


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
        repoboxls.push(new repobox(repo["name"],repo["description"],repo["lic"],repo["owner"],repo["url"],repo["lang"],repo["pfp"]))

    }
}
main()