from datetime import datetime


class Service:

    def __init__(self, name: str = None,
                 level: str = None,
                 parent: str = None,
                 create_time: datetime = datetime.utcnow(),
                 update_time: datetime = datetime.utcnow(),
                 usage: str = None,
                 is_delete: bool = False):
        self.__name = name
        self.__level = level
        self.__parent = parent
        self.__ctime = create_time
        self.__utime = update_time
        self.__usage = usage
        self.__is_delete = is_delete

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str = None):
        self.__name = name

    def get_level(self) -> str:
        return self.__level

    def set_level(self, level: str = None):
        self.__level = level

    def get_parent(self) -> str:
        return self.__parent

    def set_parent(self, parent: str = None):
        self.__parent = parent

    def get_ctime(self) -> datetime:
        return self.__ctime

    def set_ctime(self, ctime: datetime = datetime.utcnow()):
        self.__ctime = ctime

    def get_utime(self) -> datetime:
        return self.__utime

    def set_utime(self, utime: datetime = datetime.utcnow()):
        self.__utime = utime

    def get_usage(self) -> str:
        return self.__usage

    def set_usage(self, usage: str = None):
        self.__usage = usage

    def get_is_delete(self) -> bool:
        return self.__is_delete

    def set_is_delete(self, is_delete: bool = False):
        self.__is_delete = is_delete
