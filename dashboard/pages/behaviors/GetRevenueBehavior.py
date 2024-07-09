from pages.behaviors.GetLineValueBehavior import GetLineValueBehavior


class GetRevenueBehavior(GetLineValueBehavior):
    def __init__(self, app):
        super().__init__(app)

    def update_new_data(self):
        self.data = self.app.databaseManager.get_revenue()
