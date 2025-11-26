from entities.Request import Request

class ViewRequestController:
    def __init__(self, user_id, role_id):
        self.user_id = user_id
        self.role_id = role_id

    def viewRequests(self, user_id, role_id):
        request = Request()
        return request.viewRequests(user_id, role_id)
