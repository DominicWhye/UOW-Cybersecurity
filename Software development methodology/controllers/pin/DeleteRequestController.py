from entities.Request import Request

class DeleteRequestController:
    def __init__(self, request_id):
        self.request_id = request_id
    
    def deleteRequest(self, request_id):
        request = Request()
        return request.deleteRequest(request_id)