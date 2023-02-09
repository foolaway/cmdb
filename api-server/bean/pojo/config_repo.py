from datetime import datetime


class ConfigRepo:
    def __init__(self, name: str = None,
                 address: str = None,
                 _type: str = None,
                 create_time: datetime = datetime.utcnow(),
                 update_time: datetime = datetime.utcnow(),
                 usage: str = None,
                 is_delete: bool = False
                 ):
        self.__name = name,
        self.__address = address
        self.__type = _type
        self.__ctime = create_time
        self.__utime = update_time
        self.__usage = usagey
        self.__is_delete = is_delete

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str = None):
        self.__name = name

    def get_address(self) -> str:
        return self.__address

    def set_address(self, address: str = None):
        self.__address = address

    def get_type(self) -> str:
        return self.__type

    def set_type(self, _type: str = None):
        self.__type = _type

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
