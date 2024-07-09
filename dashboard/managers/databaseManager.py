import pandas as pd
from managers.constants.index import DATA_KEYS


FILE_PATH = "managers/data/banks-n-nonbanking.csv"


class DatabaseManager:
    data_keys: dict

    def __init__(self):
        self.data = pd.read_csv(FILE_PATH, index_col=0).sort_values(
            by="year", ascending=False
        )
        self.symbol = ""

    def set_symbol(self, symbol):
        self.symbol = symbol

        if self.is_banking():
            self.data_keys = DATA_KEYS["BANK"]
        else:
            self.data_keys = DATA_KEYS["NON_BANK"]

        return self

    def get_all_company_names(self):
        return self.data["code"].unique()

    def get_revenue(self, y_range=4):
        return self._get_fin_metrics([self.data_keys["REVENUE"]], y_range)

    def get_gross_income(self, y_range=4):
        return self._get_fin_metrics([self.data_keys["GROSS_INCOME"]], y_range)

    def get_expenses(self, y_range=4):
        return self._get_fin_metrics([self.data_keys["EXPENSES"]], y_range)

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
