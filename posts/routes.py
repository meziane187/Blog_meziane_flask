from flask import render_template
from flask import Blueprint
posts_blueprint=Blueprint  ('blog', __name__, template_folder='templates')
from models import Post



@posts_blueprint.route('/')
def list_of_posts():
    posts = Post.query.all()
    print (posts)
    return render_template ("posts.html", posts=posts)