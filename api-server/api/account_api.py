from flask import Blueprint


class AccountAPI:
    bp_account = Blueprint("account", __name__, "/account")
