import dash
import dash_bootstrap_components as dbc
from dash import dcc
from pages.components.Navbar import Navbar


class AppLayout(dbc.Container):
    def __init__(self, app):
        self.app = app
        self.create()

        super().__init__(
            self.elements,
            fluid=True,
            className="dbc",
        )

    def create(self):
        self.elements = [
            dcc.Location(id="url", refresh=False),
            dbc.Row(
                Navbar(app=self.app, height=5),
            ),
            dbc.Row(dash.page_container),
        ]
