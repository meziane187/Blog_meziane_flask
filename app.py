import os

from flask import Flask
from dotenv import load_dotenv

from posts import routes
load_dotenv()


app = Flask(__name__)

config_object = os.environ.get("CONFIG")
if config_object:
    app.config.from_object(config_object)
else:
    print("Config not found")

app.register_blueprint(routes.posts_blueprint, url_prefix='/blog')

