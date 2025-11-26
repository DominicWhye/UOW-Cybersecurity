from entities.Request import Request

class UpdateRequestController:
    def __init__(self):
        pass

    def getRequestById(self, request_id):
        """Fetch a single request by its ID (no ownership checks)."""
        req = Request()
        return req.getRequestById(request_id)
    
    def updateRequest(self, category_id, request_id):
        request = Request()
        return request.updateRequest(category_id, request_id)