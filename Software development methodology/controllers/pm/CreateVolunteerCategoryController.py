from entities.Category import Category

class CreateVolunteerCategoryController:
    def __init__(self):
        pass

    def createVolunteerCategory(self, category_name, category_desc):
        category = Category(
            category_name=category_name,
            category_desc=category_desc
        )

        return category.createVolunteerCategory(category_name, category_desc)
