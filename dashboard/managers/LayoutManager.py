import dash
import dash_bootstrap_components as dbc
from dash import dcc
from interfaces.index import IApp
from pages.components.Navbar import Navbar


class LayoutManager(dbc.Container):
    def __init__(self, app):
        self.app: IApp = app
        self.__create()

        super().__init__(
            self.elements,
            fluid=True,
            className="dbc",
        )

    def __create(self):
        self.elements = [
            dcc.Location(id="url", refresh=False),
            dbc.Row(
                Navbar(app=self.app, height=5),
            ),
            dbc.Row(dash.page_container),
        ]
