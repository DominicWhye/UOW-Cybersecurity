from entities.Request import Request

class CreateRequestController:
    def __init__(self, user_id):
        self.user_id = user_id

    def createRequest(self, category_id):
        """Create a new request for this user."""
        request = Request()
        return request.createRequest(self.user_id, category_id)