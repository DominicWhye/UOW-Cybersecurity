from entities.Request import Request

class ViewCompletedServicesController:
    def __init__(self):
        pass
   
    def viewCompletedServices(self, user_id):
        request = Request()
        return request.viewCompletedServices(user_id)