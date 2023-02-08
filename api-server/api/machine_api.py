from flask import Blueprint, request

from service.machine_service import MachineService
from util.request_util import RequestUtil
from util.string_util import StringUtil


class MachineAPI:
    bp_machine_api = Blueprint("machine", __name__, "/machine")

    @staticmethod
    @bp_machine_api.route("/<uuid>", methods=("GET",))
    def get_machine_by_uuid(uuid):
        MachineService.get_machine_by_uuid(StringUtil.smart_trim(uuid))

        return {}

    @staticmethod
    @bp_machine_api.route("/", methods=("GET",))
    def get_machine():
        p_service = RequestUtil.get_param_from_url_query_param(request, "service")
        p_res_pool = RequestUtil.get_param_from_url_query_param(request, "res-pool")
        p_type = RequestUtil.get_param_from_url_query_param(request, "type")
        p_status = RequestUtil.get_param_from_url_query_param(request, "status")

        service = StringUtil.smart_trim(p_service)
        res_pool = StringUtil.smart_trim(p_res_pool)
        _type = StringUtil.smart_trim(p_type)
        status = StringUtil.smart_trim(p_status)

        MachineService.list_machine(service, res_pool, _type, status)

        return {}





