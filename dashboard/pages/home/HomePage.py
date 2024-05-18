import dash
import dash_bootstrap_components as dbc
from dash import html
from pages.components.CashFlowFallGraph import CashFlowFallGraph
from pages.components.DeptEquityGraph import DeptEquityGraph
from pages.components.DupontRatiosGraph import DupontRatiosGraph
from pages.components.CashFlowGraph import CashFlowGraph
from pages.components.FirstGraphsRow import FirstGraphsRow
from pages.components.BreakdownRevenueGraph import BreakdownRevenueGraph


class HomePage:
    def __init__(self):
        self.layout = dbc.Container(
            [
                dbc.Row([html.P("Navbar")], style={"height": "5vh"}),
                FirstGraphsRow(height=30),
                dbc.Row(
                    [
                        dbc.Col(CashFlowGraph(height=30), width=6),
                        dbc.Col(BreakdownRevenueGraph(height=30), width=6),
                    ],
                    className="g-2 custom_row",
                ),
                dbc.Row(
                    [
                        dbc.Col(DupontRatiosGraph(height=29), width=4),
                        dbc.Col(
                            DeptEquityGraph(
                                height=29,
                            ),
                            width=4,
                        ),
                        dbc.Col(CashFlowFallGraph(height=29), width=4),
                    ],
                    className="g-2 custom_row",
                ),
            ],
            fluid=True,
            className="dbc",
            style={"background-color": "#f2f2f2"},
        )


dash.register_page(__name__, path="/")
layout = HomePage().layout
