import dash
from dash import html
import dash_bootstrap_components as dbc


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(
            dbc.NavLink("About", href="/about"),
        ),
    ],
    brand="Capital Vision",
    brand_href="#",
    color="primary",
    dark=True,
    fluid=True,
    sticky="top",
)

sidebar = html.Div(
    [
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [html.I(className="fas fa-home me-2"), html.Span("Home")],
                    href="/",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-chart-simple me-2"),
                        html.Span("Stock"),
                    ],
                    href="/stock",
                    active="exact",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)


layout = dbc.Container(
    [
        navbar,
        html.Div(
            [sidebar, dash.page_container],
            className="content",
        ),
    ],
    fluid=True,
    className="dbc",
)
