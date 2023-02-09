from datetime import datetime


class TaskDetail:
    def __init__(self,
                 _id: str = None,
                 machine_id: str = None,
                 status: str = None,
                 create_time: datetime = datetime.utcnow(),
                 update_time: datetime = datetime.utcnow(),
                 is_delete: bool = False,
                 ):
        self.__id = _id
        self.__machine_id = machine_id
        self.__ctime = create_time
        self.__utime = update_time
        self.__status = status
        self.__is_delete = is_delete

    def get_id(self) -> str:
        return self.__id

    def set_id(self, _id: str = None):
        self.__id = _id

    def get_machine_id(self) -> str:
        return self.__machine_id

    def set_machine_id(self, machine_id: str = None):
        self.__machine_id = machine_id

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
