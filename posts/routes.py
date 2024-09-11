from flask import render_template
from flask import Blueprint
posts_blueprint=Blueprint  ('blog', __name__, template_folder='templates')


@posts_blueprint.route('/')
def list_of_posts():
    name = "meziane"
    return render_template("posts.html", name=name)