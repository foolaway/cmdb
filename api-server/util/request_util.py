class RequestUtil:
    @staticmethod
    def get_param(request, name: str):
        request_context = request.json

        value = None

        try:
            value = request_context[name]
        except KeyError:
            print("发生 KeyError 错误...")

        return value

