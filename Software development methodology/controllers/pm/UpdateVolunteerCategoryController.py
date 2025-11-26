from entities.Category import Category

class UpdateVolunteerCategoryController:
    def __init__(self):
        pass

    def getCategoryById(self, category_id):
        category = Category()
        return category.getCategoryById(category_id)

    def updateVolunteerCategory(self, category_id, category_name, category_desc):
        category_account = Category(
            category_id=category_id,
            category_name=category_name,
            category_desc=category_desc
        )
        return category_account.updateVolunteerCategory(category_id, category_name, category_desc)