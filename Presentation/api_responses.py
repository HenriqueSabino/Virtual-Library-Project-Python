class APIResponse:
    def __init__(self, status: str, message: str, data: any = None):
        self.status = status
        self.message = message
        self.data = data

def success(message: str, data: any = None):
    return APIResponse("success", message, data).__dict__

def error(message: str):
    return APIResponse("error", message).__dict__