import pandas as pd
import os


FILE_PATH = "dashboard/models/asx200_data.csv"


class FinancialMetrics:
    def __init__(self):
        self.data = pd.read_csv(FILE_PATH, index_col=0).sort_values(
            by="report_year", ascending=False
        )

    def symbol(self, symbol):
        self.symbol = symbol
        return self

    def get_fin_metrics(self, metrics, y_range):
        res_df = self.data.sort_values(by="report_year", ascending=False)
        query_years = self.data.query("code == @self.symbol")["report_year"].unique()[
            :5
        ]
        res_df = self.data.query(
            f""" \
                    code == @self.symbol and \
                    report_year in @query_years and \
                    metrics in @metrics
                """
        )
        return res_df
