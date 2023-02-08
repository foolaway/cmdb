from flask import Blueprint


class ResPoolAPI:
    bp_res_pool_api = Blueprint("res_pool", __name__, url_prefix="/res_pool")
