from entities.Category import Category    

class ViewVolunteerCategoryController:
    def viewVolunteerCategory(self):
        categories = Category()
        return categories.viewVolunteerCategory()