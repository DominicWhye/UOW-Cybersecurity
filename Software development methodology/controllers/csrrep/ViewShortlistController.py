from entities.Shortlist import Shortlist

class ViewShortlistController:
    def __init__(self):
        pass
   
    def viewShortlist(self, csrrep_user_id):
        shortlist = Shortlist()
        return shortlist.viewShortlist(csrrep_user_id)