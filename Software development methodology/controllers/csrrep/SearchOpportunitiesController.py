from entities.Request import Request


class SearchOpportunitiesController:
    
    def __init__(self):
        pass

    def searchOpportunities(self, keyword):
        request = Request()
        return request.searchOpportunities(keyword)