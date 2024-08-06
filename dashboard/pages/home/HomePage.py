import dash_bootstrap_components as dbc
from pages.components.PageLayout import PageLayout
from pages.home.components.SearchBar import SearchBar
from pages.home.components.LeverageRatioGraph import LeverageRatioGraph
from pages.home.components.PayoutRatioGraph import PayoutRatioGraph
from pages.home.components.AnualCashFlow import AnualCashFlow
from pages.home.components.DeptEquityGraph import DebtEquityGraph
from pages.home.components.BreakDownCashFlow import BreakDownCashFlow
from pages.home.components.FirstGraphsRow import FirstGraphsRow
from dash import callback, Output, Input


class HomePage:
    layout: dbc.Container

    def __init__(self, app):
        self.app = app

        self.__create()

        self.layout = PageLayout(
            [
                self.search_bar,
                self.first_graphs_row,
                dbc.Row(
                    [
                        dbc.Col(BreakDownCashFlow(height=30), width=6),
                        dbc.Col(
                            self.payout_ratio_graph,
                            width=6,
                        ),
                    ],
                    className="g-2 custom_row",
                ),
                dbc.Row(
                    [
                        dbc.Col(LeverageRatioGraph(height=29), width=4),
                        dbc.Col(
                            DebtEquityGraph(
                                height=29,
                            ),
                            width=4,
                        ),
                        dbc.Col(AnualCashFlow(height=29), width=4),
                    ],
                    className="g-2 custom_row",
                ),
            ]
        )

        self.__enable_callbacks()

    def __create(self):
        self.search_bar = SearchBar(app=self.app, height=4)
        self.first_graphs_row = FirstGraphsRow(height=28, app=self.app)
        self.payout_ratio_graph = PayoutRatioGraph(
            height=30, observable=self.app.databaseManager
        )

    def __enable_callbacks(self):
        self.search_bar.enable_callback()
        self.first_graphs_row.enable_callback()
        self.__enable_payout_callback()

    def __enable_payout_callback(self):
        @callback(
            Output(self.payout_ratio_graph.graph_id, "figure"),
            Input("company-title", "children"),
        )
        def display_data(children):
            return self.payout_ratio_graph.create_figure()
