import pandas as pd
import os
from managers.constants.index import DATA_KEYS


FILE_PATH = "dashboard/managers/constants/asx200_data.csv"


class DatabaseManager:
    def __init__(self):
        self._data = pd.read_csv(FILE_PATH, index_col=0).sort_values(
            by="report_year", ascending=False
        )
        self._symbol = ""

    def set_symbol(self, symbol):
        self._symbol = symbol
        return self

    def get_company_names(self):
        return self._data["company_name"].unique()

    def get_revenue(self, y_range):
        return self._get_fin_metrics([DATA_KEYS["REVENUE"]], y_range)

    def _get_fin_metrics(self, metrics, y_range=5):
        res_df = self._data.sort_values(by="report_year", ascending=False)
        query_years = self._data.query("code == @self._symbol")["report_year"].unique()[
            :y_range
        ]
        res_df = self._data.query(
            f""" \
                    code == @self._symbol and \
                    report_year in @query_years and \
                    metrics in @metrics
                """
        )
        print(123, res_df)
        return res_df
