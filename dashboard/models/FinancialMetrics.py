import pandas as pd
import os


FILE_PATH = "models/banks-n-nonbanking.csv"


class FinancialMetrics:
    def __init__(self):
        self.data = pd.read_csv(FILE_PATH, index_col=0).sort_values(
            by="year", ascending=False
        )

    def symbol(self, symbol):
        self.symbol = symbol
        return self

    def get_fin_metrics(self, metrics, y_range=5):
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
