import dash
from dash import html
import dash_bootstrap_components as dbc
from pages.components.sidebar import sidebar


def layout():
    return dbc.Row(
        [
            dbc.Container(
                [
                    html.Div(
                        [sidebar(), dash.page_container],
                        className="content",
                    ),
                ],
                fluid=True,
                className="dbc",
            )
        ]
    )
