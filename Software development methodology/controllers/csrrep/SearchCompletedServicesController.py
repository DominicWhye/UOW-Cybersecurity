from entities.Request import Request

class SearchCompletedServicesController:
    def __init__(self):
        pass
   
    def searchCompletedServices(self, user_id, keyword):
        opportunity = Request()
        return opportunity.SearchCompletedServices(user_id, keyword)