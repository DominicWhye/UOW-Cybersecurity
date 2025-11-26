from entities.Shortlist import Shortlist

class SearchShortlistController:
    def __init__(self):
        pass
   
    def searchShortlist(self, user_id, keyword):
        shortlist = Shortlist()
        return shortlist.searchShortlist(user_id, keyword)