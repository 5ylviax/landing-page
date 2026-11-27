from flask import Flask, render_template, send_from_directory
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR / "data" / "projects.json", encoding="utf-8") as file:
    PROJECTS = json.load(file)

with open(BASE_DIR / "data" / "gallery.json", encoding="utf-8") as file:
    GALLERY = json.load(file)
    
app = Flask(__name__)


# SEO
@app.route("/sitemap.xml")
def sitemap():
    return send_from_directory(
        app.static_folder,
        "sitemap.xml",
        mimetype="application/xml"
    )


@app.route("/robots.txt")
def robots():
    return send_from_directory(
        app.static_folder,
        "robots.txt",
        mimetype="text/plain"
    )


# Website Routes
@app.route("/")
def index():
    return render_template("home.html", name="Silvia Saavedra")


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
    app.run(debug=False)
