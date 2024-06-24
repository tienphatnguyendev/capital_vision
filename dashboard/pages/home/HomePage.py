import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash import html
from pages.components.LeverageRatioGraph import LeverageRatioGraph
from pages.components.PayoutRatioGraph import PayoutRatioGraph
from pages.components.AnualCashFlow import AnualCashFlow
from pages.components.DeptEquityGraph import DeptEquityGraph
from pages.components.BreakDownCashFlow import BreakDownCashFlow
from pages.components.FirstGraphsRow import FirstGraphsRow


class HomePage:
    def __init__(self, app):
        self.app = app
        self.layout = dbc.Container(
            [
                dcc.Interval(
                    id="interval-component",
                    interval=1000 // 60,
                    n_intervals=0,
                ),
                dbc.Row([html.P("Navbar")], style={"height": "5vh"}),
                FirstGraphsRow(height=32, app=self.app),
                dbc.Row(
                    [
                        dbc.Col(BreakDownCashFlow(height=30), width=6),
                        dbc.Col(PayoutRatioGraph(height=30), width=6),
                    ],
                    className="g-1 custom_row",
                ),
                dbc.Row(
                    [
                        dbc.Col(LeverageRatioGraph(height=30), width=4),
                        dbc.Col(
                            DeptEquityGraph(
                                height=30,
                            ),
                            width=4,
                        ),
                        dbc.Col(AnualCashFlow(height=30), width=4),
                    ],
                    className="g-1 custom_row",
                ),
            ],
            fluid=True,
            className="dbc",
            style={"background-color": "#ffffff", "height": "100vh"},
        )

        dash.register_page(__name__, path="/", layout=self.layout)
