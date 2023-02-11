import datetime

from flask_restful import fields


class GroupDTO:
    # ___id = None
    # __name = None
    # __usage = None
    # __create_time = None
    # __update_time = None

    fields = {
        "name": fields.String,
        "usage": fields.String,
        "ctime": fields.DateTime(attribute="create_time"),
        "utime": fields.DateTime(attribute="update_time")
    }

    def __init__(self, name: str = None,
                 usage: str = None,
                 create_time: datetime = datetime.datetime.utcnow(),
                 update_time: datetime = datetime.datetime.utcnow(),
                 is_delete: bool = None):
        self.name = name
        self.usage = usage
        self.create_time = create_time
        self.update_time = update_time
        self.is_delete = is_delete

    def get_name(self) -> str:
        return self.name

    def get_usage(self) -> str:
        return self.usage

    def get_create_time(self) -> datetime:
        return self.create_time

    def get_update_time(self) -> datetime:
        return self.update_time

    def set_create_time(self, ctime: datetime):
        self.create_time = ctime

    def set_update_time(self, utime: datetime):
        self.update_time = utime

    def set_name(self, name: str):
        self.name = name

    def set_usage(self, usage: str):
        self.usage = usage

    def set_is_delete(self, is_delete: bool):
        self.is_delete = is_delete

    def get_is_delete(self) -> bool:
        return self.is_delete
