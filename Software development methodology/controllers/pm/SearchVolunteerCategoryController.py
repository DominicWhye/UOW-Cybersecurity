from entities.Category import Category    

class SearchVolunteerCategoryController:
    def searchVolunteerCategory(self, keyword):
        categories = Category()
        return categories.searchVolunteerCategory(keyword)