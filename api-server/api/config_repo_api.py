from flask import Blueprint

from util.request_util import RequestUtil
from util.string_util import StringUtil

class ConfigRepoAPI:
    bp_config_repo_api = Blueprint("config_repo", __name__, url_prefix="/config_repo")

    @staticmethod
    @bp_config_repo_api.route("/<name>", methods=("GET", ))
    def get_config_repo_by_name(name):


        return {}

    @staticmethod
    @bp_config_repo_api.route("/", methods=("GET", ))
    def list_config_repo():

        return {}

    @staticmethod
    @bp_config_repo_api.route("/", methods=("POST", ))
    def create_config_repo():
        return {}

    @staticmethod
    @bp_config_repo_api.route("/<name>", methods=("PUT", ))
    def update_config_repo_by_name(name):
        return {}

    @staticmethod
    @bp_config_repo_api.route("/<name>", methods=("DELETE",))
    def delete_config_repo_by_name(name):
        return {}

    @staticmethod
    @bp_config_repo_api.route("/", methods=("DELETE",))
    def delete_config_repo():

        return {}
