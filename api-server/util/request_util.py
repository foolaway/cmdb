class RequestUtil:
    @staticmethod
    def get_param_from_body_raw_json(request, name: str):
        request_context = request.json

        value = None

        try:
            value = request_context[name]
        except KeyError:
            print("发生 KeyError 错误...")

        return value

    @staticmethod
    def get_param_from_body_raw_json_as_list(request):
        if type(request.json) is list:
            return request.json

        return []

    @staticmethod
    def get_param_from_url_query_param(request, name):
        request_values = request.values

        # get 获取不到默认返回 None
        value = request_values.get(name)

        return value
