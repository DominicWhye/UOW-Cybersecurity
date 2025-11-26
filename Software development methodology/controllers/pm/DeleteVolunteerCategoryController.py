from entities.Category import Category    

class DeleteVolunteerCategoryController:
    def __init__(self, category_id):
        self.category_id = category_id
    
    def deleteVolunteerCategory(self, category_id):
        categories = Category()
        return categories.deleteVolunteerCategory(category_id)