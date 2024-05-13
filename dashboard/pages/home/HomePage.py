import dash
import dash_bootstrap_components as dbc
from dash import html
from pages.components.FirstGraphsRow import FirstGraphsRow
from pages.components.BreakdownRevenueGraph import BreakdownRevenueGraph


class HomePage:
    def __init__(self):
        self.layout = dbc.Container(
            [
                dbc.Row([html.P("Navbar")], style={"height": "70px"}),
                FirstGraphsRow(),
                dbc.Row(
                    [
                        dbc.Col(
                            BreakdownRevenueGraph(),
                        ),
                    ],
                    className="g-2 custom_row",
                ),
            ],
            fluid=True,
            className="dbc",
        )


dash.register_page(__name__, path="/")
layout = HomePage().layout
