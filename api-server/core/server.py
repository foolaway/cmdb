from flask import Flask
from flask_pymongo import PyMongo
from .settings import settings


class Server:
    app = Flask(__name__)

    datasource = {}

    for item in settings["datasource"]:
        if item["type"] == "mongodb":
            uri = "mongodb://" + item["host"] + ":" + item["port"] + "/" + item["database"]
            mongo_client = PyMongo(app, uri)
            datasource[item["name"]] = mongo_client
            print("[INFO]: connect to '{}' as '{}'".format(uri, item["name"]))

            # app.config["MONGO_URI"] = "mongodb://192.168.111.223:27017/db_gala_cmdb"
            # mongo_client = PyMongo(app)

