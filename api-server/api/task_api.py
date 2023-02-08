import datetime
import uuid

from flask import Blueprint, request

from service.task_service import TaskService
from util.string_util import StringUtil
from util.request_util import RequestUtil


class TaskAPI:
    bp_task_api = Blueprint("task", __name__, url_prefix="/task")

    @staticmethod
    @bp_task_api.route("/", methods=("POST",))
    def create_task():
        """
        创建一个新的配置下发任务, 返回任务 ID
        :return:
        """
        p_repo = RequestUtil.get_param_from_body_raw_json(request, "repo")
        p_branch = RequestUtil.get_param_from_body_raw_json(request, "branch")
        p_tag = RequestUtil.get_param_from_body_raw_json(request, "tag")
        p_target_directory = RequestUtil.get_param_from_body_raw_json(request, "target-directory")
        p_post_sync_script = RequestUtil.get_param_from_body_raw_json(request, "post-sync-script")
        p_machines = RequestUtil.get_param_from_body_raw_json(request, "machines")
        p_services = RequestUtil.get_param_from_body_raw_json(request, "services")
        p_webhook_url = RequestUtil.get_param_from_body_raw_json(request, "webhook_url")
        p_webhook_sign = RequestUtil.get_param_from_body_raw_json(request, "webhook-sign")

        create_time = datetime.datetime.now()
        update_time = datetime.datetime.now()
        status = "已提交"
        timeout = None
        retry = 3

        repo = StringUtil.smart_trim(p_repo)
        branch = StringUtil.smart_trim(p_branch)
        tag = StringUtil.smart_trim(p_tag)
        target_directory = StringUtil.smart_trim(p_target_directory)
        post_sync_script = StringUtil.smart_trim(p_post_sync_script)
        machines = StringUtil.smart_trim(p_machines)
        services = StringUtil.smart_trim(p_services)
        webhook_url = StringUtil.smart_trim(p_webhook_url)
        webhook_sign = StringUtil.smart_trim(p_webhook_sign)

        _id = str(uuid.uuid4())

        TaskService.create_task(_id, repo, branch, tag, target_directory, post_sync_script, machines, services,
                                webhook_url, webhook_sign)

        return {}

    @staticmethod
    @bp_task_api.route("/repo-check/<_id>", methods=("GET", ))
    def repo_check_phase(_id):
        """
        查询配置数据存储库状态是否可用
        :param _id:
        :return:
        """
        TaskService.get_repo_check_phase_info(StringUtil.smart_trim(_id))

        return {}

    @staticmethod
    @bp_task_api.route("/running/<_id>", methods=("GET", ))
    def running_phase(_id):
        """
        返回正在执行时,剩余的机器数量
        :param _id:
        :return:
        """
        TaskService.get_running_phase_info(StringUtil.smart_trim(_id))

        return {}

    @staticmethod
    @bp_task_api.route("/result/<_id>", methods=("GET",))
    def result_phase(_id):
        """
        返回任务执行结果
        :param _id:
        :return:
        """
        TaskService.get_result_phase_info(StringUtil.smart_trim(_id))

        return {}





