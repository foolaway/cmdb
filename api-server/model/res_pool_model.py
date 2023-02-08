from flask import Blueprint, request

from service.res_pool_service import ResPoolService
from util.request_util import RequestUtil
from util.string_util import StringUtil


class ResPoolAPI:
    res_pool_api = Blueprint("res_pool", __name__, url_prefix="/res-pool")

    @staticmethod
    @res_pool_api.route("/<name>", methods=("GET",))
    def get_res_pool_by_name(name):
        ResPoolService.get_res_pool_by_name(StringUtil.smart_trim(name))

        return {}

    @staticmethod
    @res_pool_api.route("/", methods="GET", )
    def list_res_pool():
        p_usage = RequestUtil.get_param_from_url_query_param(request, "usage")

        usage = StringUtil.smart_trim(p_usage)

        ResPoolService.list_res_pool(usage)

        return {}
