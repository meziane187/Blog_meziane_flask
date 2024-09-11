import os

from models import Post,db
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from posts import routes
load_dotenv()



app = Flask(__name__)

config_object = os.environ.get("CONFIG")
if config_object:
    app.config.from_object(config_object)
else:
    print("Config not found")

app.register_blueprint(routes.posts_blueprint, url_prefix='/blog')
db.init_app(app)








