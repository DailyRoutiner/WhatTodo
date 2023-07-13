from app import app
from flask import render_template
from app import database

@app.route("/")
def home():
    return render_template("index.html", name=database.get_name())
# The variable we assign here can be used in the html using double curly brackest, as {{name}}