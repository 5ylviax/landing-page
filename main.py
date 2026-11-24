from flask import Flask, render_template

app = Flask(__name__)

PROJECTS = [
    {
        "title": "Jacob Grub's",
        "description": "This site. Built with Flask, Jinja templates and plain CSS.",
        "image": None,
        "url": "https://jacobsgrub.duckdns.org/",
    },
]

@app.route("/")
def index():
    return render_template("home.html", name="Silvia")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html", projects=PROJECTS)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
