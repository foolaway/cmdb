from bean.pojo.group import Group
from core.server import Server


class GroupModel:
    @staticmethod
    def get_group_by_name(name: str) -> Group:
        result = Server.datasource["default"].db["group"].find({'_id': {"$regex": name}})

        groups = []
        for item in result:
            groups.append(Group(name=item["_id"],
                                usage=item["usage"],
                                create_time=item["create_time"],
                                update_time=item["update_time"]))
        return groups

    @staticmethod
    def all_group(usage: str | None):
        if usage is None:
            result = Server.datasource["default"].db["group"].find({"is_delete": False})
            groups = []
            for item in result:
                groups.append(Group(name=item["_id"],
                                    usage=item["usage"],
                                    create_time=item["create_time"],
                                    update_time=item["update_time"]))

            return groups
        else:
            result = Server.datasource["default"].db["group"].find({"usage": usage})
            return result
