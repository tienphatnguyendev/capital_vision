import dash_bootstrap_components as dbc
from pages.home.components.SearchBar import SearchBar
from pages.home.components.LeverageRatioGraph import LeverageRatioGraph
from pages.home.components.PayoutRatioGraph import PayoutRatioGraph
from pages.home.components.AnualCashFlow import AnualCashFlow
from pages.home.components.DeptEquityGraph import DeptEquityGraph
from pages.home.components.BreakDownCashFlow import BreakDownCashFlow
from pages.home.components.FirstGraphsRow import FirstGraphsRow


class HomePage:
    layout: dbc.Container

    def __init__(self, app):
        self.app = app
        self.layout = dbc.Container(
            [
                SearchBar(app=self.app, height=4),
                FirstGraphsRow(height=28, app=self.app),
                dbc.Row(
                    [
                        dbc.Col(BreakDownCashFlow(height=30), width=6),
                        dbc.Col(PayoutRatioGraph(height=30), width=6),
                    ],
                    className="g-2 custom_row",
                ),
                dbc.Row(
                    [
                        dbc.Col(LeverageRatioGraph(height=29), width=4),
                        dbc.Col(
                            DeptEquityGraph(
                                height=29,
                            ),
                            width=4,
                        ),
                        dbc.Col(AnualCashFlow(height=29), width=4),
                    ],
                    className="g-2 custom_row",
                ),
            ],
            fluid=True,
            className="dbc",
            style={"height": "95vh"},
        )
