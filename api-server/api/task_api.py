from flask import Blueprint


class TaskAPI:
    bp_task_api = Blueprint("task", __name__, url_prefix="/task")
