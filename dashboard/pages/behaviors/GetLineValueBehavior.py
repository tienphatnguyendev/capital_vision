from pandas import DataFrame
from interfaces.index import IApp


class GetLineValueBehavior:
    app: IApp
    data: DataFrame

    def __init__(self, app):
        self.app = app

    def update_new_data(self):
        pass

    def get_latest_value(self):
        self.update_new_data()
        values = self.data["value"].tolist()[::-1]
        return float(values[-1])

    def get_values(self):
        self.update_new_data()

        values = self.data["value"].tolist()[::-1]
        years = self.data["year"].tolist()[::-1]

        values = [float(value) for value in values]

        return values, years
