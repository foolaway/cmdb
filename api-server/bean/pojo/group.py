import datetime


class Group:
    # ___id = None
    # __name = None
    # __usage = None
    # __create_time = None
    # __update_time = None

    def __init__(self, name: str = None,
                 usage: str = None,
                 create_time: datetime = datetime.datetime.utcnow(),
                 update_time: datetime = datetime.datetime.utcnow(),
                 is_delete: bool = None):
        self.__name = name
        self.__usage = usage
        self.__create_time = create_time
        self.__update_time = update_time
        self.__is_delete = is_delete

    def get_name(self) -> str:
        return self.__name

    def get_usage(self) -> str:
        return self.__usage

    def get_create_time(self) -> datetime:
        return self.__create_time

    def get_update_time(self) -> datetime:
        return self.__update_time

    def set_create_time(self, ctime: datetime):
        self.__create_time = ctime

    def set_update_time(self, utime: datetime):
        self.__update_time = utime

    def set_name(self, name: str):
        self.__name = name

    def set_usage(self, usage: str):
        self.__usage = usage

    def set_is_delete(self, is_delete: bool):
        self.__is_delete = is_delete

    def get_is_delete(self) -> bool:
        return self.__is_delete
