from datetime import datetime


class Task:
    def __init__(self,
                 _id: str = None,
                 repo: str = None,
                 branch: str = None,
                 tag: str = None,
                 target_machine: list = None,
                 target_directory: list = None,
                 target_service: list = None,
                 post_sync_script: str = None,
                 webhook_url: str = None,
                 webhook_sign: str = None,
                 logs: str = None,
                 create_time: datetime = datetime.utcnow(),
                 update_time: datetime = datetime.utcnow(),
                 is_delete: bool = False,
                 status: str = None,
                 timeout: datetime = None,
                 retry: int = 3):
        self.__id = _id
        self.__repo = repo
        self.__branch = branch
        self.__tag = tag
        self.__target_machine = target_machine
        self.__target_directory = target_directory
        self.__target_service = target_service
        self.__post_sync_script = post_sync_script
        self.__webhook_url = webhook_url
        self.__webhook_sign = webhook_sign
        self.__logs = logs
        self.__ctime = create_time
        self.__utime = update_time
        self.__is_delete = is_delete
        self.__status = status
        self.__timeout = timeout
        self.__retry = retry

    def get_id(self) -> str:
        return self.__id

    def set_id(self, _id: str = None):
        self.__id = _id

    def get_repo(self) -> str:
        return self.__repo

    def set_repo(self, repo: str = None):
        self.__repo = repo

    def get_branch(self) -> str:
        return self.__branch

    def set_branch(self, branch: str = None):
        self.__branch = branch

    def get_tag(self) -> str:
        return self.__tag

    def set_tag(self, tag: str = None):
        self.__tag = tag

    def get_target_machine(self) -> list:
        return self.__target_machine

    def set_target_machine(self, target_machine: list = None):
        self.__target_machine = target_machine

    def get_target_directory(self) -> str:
        return self.__target_directory

    def get_target_service(self) -> list:
        return self.__target_service

    def set_target_service(self, target_service: list = None):
        self.__target_service = target_service

    def set_target_directory(self, target_directory: list = None):
        self.__target_directory = target_directory

    def get_post_sync_script(self) -> str:
        return self.__post_sync_script

    def set__post_sync_script(self, post_sync_script: str = None):
        self.__post_sync_script = post_sync_script

    def get_webhook_url(self) -> str:
        return self.__webhook_url

    def set_webhook_url(self, webhook_url: str = None):
        self.__webhook_url = webhook_url

    def get_webhook_sign(self) -> str:
        return self.__webhook_sign

    def set_webhook_sign(self, webhook_sign):
        self.__webhook_sign = webhook_sign

    def get_logs(self) -> str:
        return self.__logs

    def set_logs(self, logs: str = None):
        self.__logs = logs

    def get_ctime(self) -> datetime:
        return self.__ctime

    def set_ctime(self, ctime: datetime = datetime.utcnow()):
        self.__ctime = ctime

    def get_utime(self) -> datetime:
        return self.__utime

    def set_utime(self, utime: datetime = datetime.utcnow()):
        self.__utime = utime

    def get_is_delete(self) -> bool:
        return self.__is_delete

    def set_is_delete(self, is_delete: bool = False):
        self.__is_delete = is_delete

    def get_status(self) -> str:
        return self.__status

    def set_status(self, status: str = None):
        self.__status = status

    def get_timeout(self) -> datetime:
        return self.__timeout

    def set_timeout(self, timeout: datetime = None):
        self.__timeout = timeout

    def get_retry(self) -> int:
        return self.__retry

    def set_retry(self, retry: int = None):
        self.__retry = retry