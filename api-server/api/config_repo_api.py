import datetime

from flask import Blueprint, request

from service.config_repo_service import ConfigRepoService
from util.request_util import RequestUtil
from util.string_util import StringUtil


class ConfigRepoAPI:
    bp_config_repo_api = Blueprint("config_repo", __name__, url_prefix="/config_repo")

    @staticmethod
    @bp_config_repo_api.route("/<name>", methods=("GET",))
    def get_config_repo_by_name(name):
        ConfigRepoService.get_config_repo_by_name(StringUtil.smart_trim(name))
        return {}

    @staticmethod
    @bp_config_repo_api.route("/", methods=("GET",))
    def list_config_repo():
        p_type = RequestUtil.get_param_from_url_query_param(request, "type")
        p_usage = RequestUtil.get_param_from_url_query_param(request, "usage")

        _type = StringUtil.smart_trim(p_type)
        usage = StringUtil.smart_trim(p_usage)

        ConfigRepoService.list_config_repo(_type, usage)

        return {}

    @staticmethod
    @bp_config_repo_api.route("/", methods=("POST",))
    def create_config_repo():
        p_name = RequestUtil.get_param_from_url_query_param(request, "name")
        p_type = RequestUtil.get_param_from_url_query_param(request, "type")
        p_address = RequestUtil.get_param_from_url_query_param(request, "address")
        p_usage = RequestUtil.get_param_from_url_query_param(request, "usage")

        name = StringUtil.smart_trim(p_name)
        _type = StringUtil.smart_trim(p_type)
        address = StringUtil.smart_trim(p_address)
        usage = StringUtil.smart_trim(p_usage)

        create_time = datetime.datetime.now()
        update_time = datetime.datetime.now()

        ConfigRepoService.create_config_repo(name, _type, address, usage, create_time, update_time)
        return {}

    @staticmethod
    @bp_config_repo_api.route("/<name>", methods=("PUT",))
    def update_config_repo_by_name(name):
        p_type = RequestUtil.get_param_from_url_query_param(request, "type")
        p_address = RequestUtil.get_param_from_url_query_param(request, "address")
        p_usage = RequestUtil.get_param_from_url_query_param(request, "usage")

        name = StringUtil.smart_trim(name)
        _type = StringUtil.smart_trim(p_type)
        address = StringUtil.smart_trim(p_address)
        usage = StringUtil.smart_trim(p_usage)

        update_time = datetime.datetime.now()

        ConfigRepoService.update_config_repo_by_name(name, _type, address, usage, update_time)
        return {}

    @staticmethod
    @bp_config_repo_api.route("/<name>", methods=("DELETE",))
    def delete_config_repo_by_name(name):
        ConfigRepoService.delete_config_repo_by_name(StringUtil.smart_trim(name))
        return {}

    @staticmethod
    @bp_config_repo_api.route("/", methods=("DELETE",))
    def delete_config_repo():
        name_list = RequestUtil.get_param_from_body_raw_json_as_list(request)

        if len(name_list) > 0:
            ConfigRepoService.delete_config_repo(name_list)
        return {}
