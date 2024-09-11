from flask import render_template
from app import app
from posts import routes



@app.route('/')
def index():
    return render_template("index.html")


