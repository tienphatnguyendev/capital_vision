import pandas as pd
from managers.constants.index import DATA_KEYS


FILE_PATH = "dashboard/managers/data/banks-n-nonbanking.csv"


class DatabaseManager:
    data_keys: dict

    def __init__(self):
        self.data = pd.read_csv(FILE_PATH, index_col=0).sort_values(
            by="year", ascending=False
        )
        self.symbol = ""
        self.company_name = ""

        name = "ANZ Group Holdings Limited"
        self.set_company_name(name)

    def set_company_name(self, company_name):
        self.company_name = company_name
        self.symbol = self.get_symbol()

        if self.is_banking():
            self.data_keys = DATA_KEYS["BANK"]
        else:
            self.data_keys = DATA_KEYS["NON_BANK"]

        return self

    def get_symbol(self):
        return self.data.query("company_name == @self.company_name")["code"].values[0]

    def get_name(self):
        return self.data.query("code == @self.symbol")["company_name"].values[0]

    def get_all_company_names(self):
        return self.data["company_name"].unique()

    def get_revenue(self, y_range=4):
        return self._get_fin_metrics([self.data_keys["REVENUE"]], y_range)

    def get_gross_income(self, y_range=4):
        return self._get_fin_metrics([self.data_keys["GROSS_INCOME"]], y_range)

    def get_expenses(self, y_range=4):
        return self._get_fin_metrics([self.data_keys["EXPENSES"]], y_range)

    def get_liability(self, y_range=4):
        return self._get_fin_metrics([self.data_keys["LIABILITY"]], y_range)

    def is_banking(self):
        return self.data.query("code == @self.symbol")["industry"].values[0] == "Banks"

    def _get_fin_metrics(self, metrics, y_range=5):
        res_df = self.data.sort_values(by="year", ascending=False)
        query_years = self.data.query("code == @self.symbol")["year"].unique()[:y_range]
        res_df = self.data.query(
            f""" \
                    code == @self.symbol and \
                    year in @query_years and \
                    metrics in @metrics
            """
        )
        return res_df
