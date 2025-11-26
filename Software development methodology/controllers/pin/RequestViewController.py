from entities.Request import Request

class RequestViewController:
    def __init__(self,pin_user_id):
        self.pin_user_id = pin_user_id
    
    def requestViews(self, pin_user_id):
        request = Request()
        return request.requestViews(pin_user_id)
    