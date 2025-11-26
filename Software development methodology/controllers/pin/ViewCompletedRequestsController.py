from entities.Request import Request

class ViewCompletedRequestsController:
    def __init__(self):
        pass
    
    def viewCompletedRequests(self, pin_user_id):
        request = Request()
        return request.viewCompletedRequests(pin_user_id)