from dash.development.base_component import Component
import dash_bootstrap_components as dbc
from dash import dcc, callback, Input, Output, State, html
from pages.constants.constants import Colors


class Navbar(dbc.Row):
    def __init__(self, app, height):
        self.app = app
        self.create()

        super().__init__(
            self.container,
            style=dict(
                height=f"{height}vh",
            ),
            className="custom_row",
        )

        self.enable_inputs()

    def enable_inputs(self):
        @callback(
            [
                Output("link-home", "className"),
                Output("link-chat", "className"),
            ],
            [Input("url", "pathname")],
        )
        def update_active_link(pathname):
            if pathname == "/ChatPage":
                return ("nav-link", "nav-link nav-link-active")
            else:
                return (
                    "nav-link nav-link-active",
                    "nav-link",
                )

    def create(self):
        container = dbc.Container(fluid=True, className="nav_containter")

        container.children = [
            html.H3("CapVis", className="nav_title"),
            dbc.Container(
                [
                    dcc.Link("Home", href="/", className="nav-link", id="link-home"),
                    dcc.Link(
                        "Chat", href="/ChatPage", className="nav-link", id="link-chat"
                    ),
                ],
                fluid=True,
                className="nav-links-container",
            ),
        ]

        self.container = container
