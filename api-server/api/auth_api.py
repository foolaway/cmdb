import base64

from flask import Blueprint, request

from service.auth_service import AuthService
from util.request_util import RequestUtil
from util.string_util import StringUtil


class AuthAPI:
    bp_auth_api = Blueprint("auth", __name__, url_prefix="/auth")

    @staticmethod
    @bp_auth_api.route("/login", methods=('POST',))
    def login():
        p_username = RequestUtil.get_param_from_body_raw_json(request, "username")
        p_password_base64 = RequestUtil.get_param_from_body_raw_json(request, "password")

        p_password = base64.b64decode(p_password_base64).decode("UTF-8")

        username = StringUtil.smart_trim(p_username)
        passwd = StringUtil.smart_trim(p_password)

        AuthService.login(username, passwd)

        return {}

    @staticmethod
    @bp_auth_api.route("/refresh", methods=('POST',))
    def refresh():
        p_refresh = RequestUtil.get_param_from_body_raw_json(request, "refresh")
        refresh = StringUtil.smart_trim(p_refresh)

        AuthService.refresh(refresh)

        return refresh

    @staticmethod
    @bp_auth_api.route("reset-password", methods=('POST',))
    def reset_password():
        """
        忘记密码, 重置密码,向可能的通知类型发送验证码信息(邮箱, 手机号)
        :return:
        """
        p_username = RequestUtil.get_param_from_body_raw_json(request, "username")
        username = StringUtil.smart_trim(p_username)

        AuthService.reset_password(username)

        return {}

