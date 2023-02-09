from bean.pojo.group import Group
from core.server import Server


class GroupModel:
    @staticmethod
    def get_group_by_name(name: str) -> Group:
        result = Server.datasource["default"].db["group"].find_one({"_id": name})
        # print(result)
        return Group(name=result["_id"],
                     usage=result["usage"],
                     create_time=result["create_time"],
                     update_time=result["update_time"])


