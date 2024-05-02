import dash
from dash import dash_table, dcc, callback, Output, Input, html
import pandas as pd
import dash_bootstrap_components as dbc
from pages.components.header_graph import header_container
from pages.components.dupont_ratios_graph import dupont_ratios_graph
from pages.constants.constants import ELEMENT
from pages.components.sankey_graph import sankey_diagam

dash.register_page(__name__, path="/")

layout = dbc.Container(
    [
        dbc.Container(
            [
                dbc.Row(
                    header_container(),
                    style={
                        "height": "170px",
                    },
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            sankey_diagam(),
                        ),
                        dbc.Col(
                            dupont_ratios_graph(),
                        ),
                    ],
                    style={
                        "height": "300px",
                    },
                ),
            ],
            style={
                # "margin-left": f"{ELEMENT['sideBar']['width']}px",
            },
        )
    ],
    style={
        "background-color": "#f2f2f2",
        "position": "fixed",
        "top": "0",
        "right": "0",
        "bottom": "0",
        "max-width": "100%",
    },
)
