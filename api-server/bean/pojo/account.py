from datetime import datetime


class Account:
    def __init__(self, name: str = None,
                 username: str = None,
                 password: str = None,
                 phone: str = None,
                 email: str = None,
                 group: str = None,
                 sex: str = None,
                 arch_group: str = None,
                 ctime: datetime = datetime.utcnow(),
                 utime: datetime = datetime.utcnow(),
                 is_delete: bool = False):
        self.__name = name
        self.__username = username
        self.__password = password
        self.__phone = phone
        self.__email = email
        self.__group = group
        self.__sex = sex
        self.__arch_group = arch_group
        self.__ctime = ctime
        self.__utime = utime
        self.__is_delete = is_delete

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_username(self) -> str:
        return self.__username

    def set_username(self, username: str):
        self.__username = username

    def get_password(self) -> str:
        return self.__password

    def set_password(self, password: str):
        self.__password = password

    def get_phone(self) -> str:
        return self.__phone

    def set_phone(self, phone: str):
        self.__phone = phone

    def get_email(self) -> str:
        return self.__email

    def set_email(self, email: str):
        self.__email = email

    def get_group(self) -> str:
        return self.__group

    def set_group(self, group: str):
        self.__group = group

    def get_sex(self) -> str:
        return self.__sex

    def set_sex(self, sex: str):
        self.__sex = sex

    def get_arch_group(self) -> str:
        return self.__arch_group

    def set_arch_group(self, arch_group: str):
        self.__arch_group = arch_group

    def get_ctime(self) -> datetime:
        return self.__ctime

    def set_ctime(self, ctime: datetime):
        self.__ctime = ctime

    def get_utime(self) -> datetime:
        return self.__utime

    def set_utime(self, utime: datetime):
        self.__utime = utime

    def get_is_delete(self) -> bool:
        return self.__is_delete

    def set_is_delete(self, is_delete: bool):
        self.__is_delete = is_delete



