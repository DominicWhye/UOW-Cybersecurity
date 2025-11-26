from entities.Request import Request

class SearchCompletedRequestsController:
    def __init__(self,pin_user_id):
        self.pin_user_id = pin_user_id
    
    def searchCompletedRequests(self,pin_user_id, keyword):
        request = Request()
        return request.searchCompletedRequests(pin_user_id, keyword)