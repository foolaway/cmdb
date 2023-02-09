class GenericJsonResponse:
    """
    通用 Json 响应对象
    调用 GenericJsonResponse 对象的 build 方法可以返回 JSON
    要求: 传入的 data 对象需具有 to_json 方法, 如若没有,则按以下步骤处理
        传入的对象属于 str, dict, list, tuple, int 中的一种类型, 则直接返回, 否则, 返回 None
    """
    def __init__(self, data: object, message: str = None, code: str = 1000):
        self.data = data
        self.message = message
        self.code = code

    def build(self):
        # TODO
        result = None

        # 判断对象是否有 to_json 方法
        if hasattr(self.data, "to_json"):
            if callable(self.data.to_json):
                result = self.data.to_json()
        else:
            if type(self.data) in (str, dict, list, tuple, int):
                result = self.data

        return {
            "code": self.code,
            "message": self.message,
            "data": result
        }
