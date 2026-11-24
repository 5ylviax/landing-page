from flask import Flask, render_template

app = Flask(__name__)

PROJECTS = [
    {
        "title": "Jacob Grub's",
        "description": "GO, SQLite, HTML, CSS",
        "image": "jacobgrubs.png",
        "url": "https://jacobsgrub.duckdns.org/",
        "github_url": "https://github.com/m0jik/recipe_website"
    },
    
    {
        "title": "Framewatch",
        "description": "C++, Qt",
        "image": "FrameWatch-desktop-application.png",
        "github_url": "https://github.com/5ylviax/framewatch",
    },
    {
        "title": "Landing Page",
        "description": "Python, Flask, HTML, CSS",
        "image": None,
        "url": "https://www.silviasaavedra.dev/",
        "github_url": "https://github.com/5ylviax/landing-page",
    },
    
    {
        "title": "Baking Website",
        "description": "GO, HTML, CSS, JavaScript",
        "image": None,
        "url": "https://www.santiagopanaderia.com/",
        "github_url": "https://github.com/5ylviax/baking-website", 
    },
    
    {
        "title": "AI Powered Job Matching System",
        "description": "Python, Docker, OpenAI, RapidAI",
        "image": "",
        "url": None,
        "github_url": None,
    },
    
    {
        "title": "Gilga",
        "description": "C#, Unity",
        "image": "gilga.jpg",
        "url": "https://play.unity.com/en/games/d8d46218-d907-461d-8003-ad49bb4f85f1/gilga",
        "github_url": "https://github.com/5ylviax/Gilga",
    },
    
    
]

# GALLERY = [
#     {
#         "title": "Low-poly island",
#         "image": "island.png",
#         "tools": "Blender, Cycles",
#         "camera": "50mm, f/2.8",
#     },
# ]
GALLERY = [
]

@app.route("/")
def index():
    return render_template("home.html", name="Silvia")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html", projects=PROJECTS)

@app.route("/gallery")
def gallery():
    return render_template("gallery.html", gallery=GALLERY)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
