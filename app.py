import os

from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

config_object = os.environ.get("CONFIG")
if config_object:
    app.config.from_object(config_object)
else:
    print("Config not found")
