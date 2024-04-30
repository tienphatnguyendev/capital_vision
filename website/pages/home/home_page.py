import dash
from dash import dash_table, dcc, callback, Output, Input, html
import pandas as pd
import dash_bootstrap_components as dbc
from pages.components.header_graph import header_container

dash.register_page(__name__, path="/")

layout = dbc.Container(
    [
        dbc.Row(
            header_container(),
        )
    ],
    fluid=True,
    style={
        "background-color": "#f2f2f7",
        "position": "fixed",
        "top": "0",
        "right": "0",
        "bottom": "0",
    },
)
