from typing import List, Tuple
import pandas as pd
from interfaces.index import IData, IDatabaseManager
from managers.constants.index import METRICS, DataKeys


FILE_PATH = "dashboard/data/banks-n-nonbanking.csv"


class DatabaseManager(IDatabaseManager):
    def __init__(self):
        super().__init__()

        self.data = pd.read_csv(
            FILE_PATH, index_col=0, on_bad_lines="warn"
        ).sort_values(by="year", ascending=False)

        self.symbol = ""
        self.company_name = ""
        self.__data_keys = {}

        self.update("Coles Group Limited")

    def update(self, company_name):
        self.company_name = company_name
        self.symbol = self.get_symbol()

        if self.is_banking():
            self.__data_keys = METRICS["BANK"]
        else:
            self.__data_keys = METRICS["NON_BANK"]

        self.notify_observers()

    def get_symbol(self) -> str:
        return str(
            self.data.query("company_name == @self.company_name")["code"].values[0]
        )

    def get_current_name(self) -> str:
        return self.company_name

    def get_current_symbol(self) -> str:
        return self.symbol

    def get_all_company_names(self) -> list[str]:
        return [str(name) for name in self.data["company_name"].unique()]

    def is_banking(self) -> bool:
        return self.data.query("code == @self.symbol")["industry"].values[0] == "Banks"

    def get_data(self, data_key, statement_key, to_million=True) -> IData:
        data = self.get_datas(data_key, 1, statement_key, to_million)[0]
        return data

    def get_datas(
        self, data_key, year_range, statement_key, to_million=True
    ) -> list[IData]:
        metric = self.__data_keys[data_key]
        query_years = self.data.query("code == @self.symbol")["year"].unique()[
            :year_range
        ]

        data = self.data.query(
            f""" \
                    code == @self.symbol and \
                    year in @query_years and \
                    metrics == @metric and \
                    statement in @statement_key
            """
        ).sort_values(by="metrics")

        years = [int(value) for value in data["year"].tolist()[::-1]]
        months = [int(value) for value in data["month"].tolist()[::-1]]
        values = [float(value) for value in data["value"].tolist()[::-1]]

        if to_million:
            values = [self.format_value_to_millions(value) for value in values]

        datas = [
            IData(month, year, value)
            for month, year, value in zip(months, years, values)
        ]

        unique_years = set(years)
        latest_month_datas = []

        for year in unique_years:
            year_data = [data for data in datas if data.year == year]
            largest_month_data = max(year_data, key=lambda x: x.month)
            latest_month_datas.append(largest_month_data)

        latest_month_datas = sorted(latest_month_datas, key=lambda x: x.year)

        return latest_month_datas

    def format_value_to_millions(self, value: float) -> float:
        return value * 1_000_000
