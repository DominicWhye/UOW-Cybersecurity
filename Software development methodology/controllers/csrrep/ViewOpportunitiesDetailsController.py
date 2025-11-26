from entities.Request import Request

class ViewOpportunitiesDetailsController:
    def __init__(self):
        pass
   
    def viewOpportunitiesDetails(self, request_id):
        request = Request()
        return request.viewOpportunitiesDetails(request_id)