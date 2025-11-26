from entities.Shortlist import Shortlist

class AddToShortlistController:
    def __init__(self):
        pass
   
    def addToShortlist(self, request_id,csrrep_user_id):
        shortlist = Shortlist()
        return shortlist.addToShortlist(request_id,csrrep_user_id)