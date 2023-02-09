from datetime import datetime


class ResPool:

    def __init__(self, name: str = None,
                 memory: float = -1.0,
                 processor: int = -1,
                 storage: float = -1.0,
                 network: float = -1.0,
                 create_time: datetime = datetime.utcnow(),
                 update_time: datetime = datetime.utcnow(),
                 usage: str = None,
                 is_delete: bool = False):
        self.__name = name
        self.__memory = memory
        self.__processor = processor
        self.__storage = storage
        self.__network = network
        self.__ctime = create_time
        self.__utime = update_time
        self.__usage = usage
        self.__is_delete = is_delete

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str = None):
        self.__name = name

    def get_memory(self) -> float:
        return self.__memory

    def set_memory(self, memory: float = 0):
        self.__memory = memory

    def get_processor(self) -> float:
        return self.__processor

    def set_processor(self, processor: int = 0):
        self.__processor = processor

    def get_storage(self) -> float:
        return self.__storage

    def set_storage(self, storage: float = 0):
        self.__storage = storage

    def get_network(self) -> float:
        return self.__network

    def set_network(self, network: float = 0):
        self.__network = network

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
