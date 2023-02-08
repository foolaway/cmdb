from flask import Blueprint


class OverviewAPI:
    bp_over_view_api = Blueprint("overview", __name__, url_prefix="/overview")
