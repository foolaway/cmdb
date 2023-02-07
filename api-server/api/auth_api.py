from flask import Blueprint, request

bp_auth = Blueprint("auth", __name__, url_prefix="/auth")


@bp_auth.route("/login", methods=('POST',))
def create():
    return "hello"

