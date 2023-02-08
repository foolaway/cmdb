import datetime

from flask import Blueprint, request

from service.account_service import AccountService
from util.request_util import RequestUtil
from util.string_util import StringUtil


class AccountAPI:
    bp_account = Blueprint("account", __name__, url_prefix="/account")

    @staticmethod
    @bp_account.route("/<uid>", methods=("GET",))
    def get_account(uid):
        """
        根据工号进行精确搜索
        :param uid:
        :return:
        """

        AccountService.get_account_by_uid(uid)
        return {}

    @staticmethod
    @bp_account.route("/", methods=("GET",))
    def list_account():
        """
        根据条件进行匹配
        :return:
        """
        p_name = RequestUtil.get_param_from_url_query_param(request, "name")
        p_phone = RequestUtil.get_param_from_url_query_param(request, "phone")
        p_email = RequestUtil.get_param_from_url_query_param(request, "email")
        p_sex = RequestUtil.get_param_from_url_query_param(request, "sex")
        p_arch_group = RequestUtil.get_param_from_url_query_param(request, "arch-group")

        name = StringUtil.smart_trim(p_name)
        phone = StringUtil.smart_trim(p_phone)
        email = StringUtil.smart_trim(p_email)
        sex = StringUtil.smart_trim(p_sex)
        arch_group = StringUtil.smart_trim(p_arch_group)

        AccountService.list_account(name, phone, email, sex, arch_group)
        return {}

    @staticmethod
    @bp_account.route("/", methods=("POST",))
    def create_account():
        """
        添加用户
        :return:
        """
        p_uid = RequestUtil.get_param_from_body_raw_json(request, "uid")
        p_name = RequestUtil.get_param_from_body_raw_json(request, "name")
        p_phone = RequestUtil.get_param_from_body_raw_json(request, "phone")
        p_email = RequestUtil.get_param_from_body_raw_json(request, "email")
        p_sex = RequestUtil.get_param_from_body_raw_json(request, "sex")
        p_arch_group = RequestUtil.get_param_from_body_raw_json(request, "arch-group")

        uid = StringUtil.smart_trim(p_uid)
        name = StringUtil.smart_trim(p_name)
        phone = StringUtil.smart_trim(p_phone)
        email = StringUtil.smart_trim(p_email)
        sex = StringUtil.smart_trim(p_sex)
        arch_group = StringUtil.smart_trim(p_arch_group)

        create_time = datetime.datetime.now()
        update_time = datetime.datetime.now()
        print(create_time)

        AccountService.create_account(uid, name, phone, email, sex, arch_group, create_time, update_time)

        return {}


