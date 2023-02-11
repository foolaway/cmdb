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

    @staticmethod
    def all_group(usage: str | None):
        if usage is None:
            result = Server.datasource["default"].db["group"].find({"is_delete": False})
            print("========================None")
            print(result)
            groups = []
            for item in result:
                groups.append(Group(name=item["_id"],
                                    usage=item["usage"],
                                    create_time=item["create_time"],
                                    update_time=item["update_time"]))

            return groups
        else:
            result = Server.datasource["default"].db["group"].find({"usage": usage})
            print("========================NO None")
            print(result)
            return result
