from entities.Request import Request

class FilterCompletedRequests:
    def __init__(self):
        pass

    def filterCompletedRequests(self, pin_user_id, category_id, request_date1,request_date2):
        request = Request()
        return request.filterCompletedRequests(pin_user_id,category_id, request_date1, request_date2)