import dash_bootstrap_components as dbc
from dash import dcc, callback, Input, Output, html
from interfaces.index import IApp


class SearchBar(dbc.Row):
    def __init__(self, app: IApp, height: float):
        self.app = app
        self.__create()
        super().__init__(
            self.__container,
            style=dict(
                height=f"{height}vh",
            ),
            className="custom_row",
        )

    def enable_callback(self):
        @callback(
            Output("company-title", "children"),
            Input("dropdown", "value"),
        )
        def display_data(value):
            if value is None:
                return self.app.databaseManager.get_current_name()
            else:
                self.app.databaseManager.update(value)
                return value

    def __create(self):
        self.__container = dbc.Container(fluid=True, className="search-bar-container")

        names = self.app.databaseManager.get_all_company_names()
        current_name = self.app.databaseManager.get_current_name()

        search_holder = dbc.Container(
            [
                dcc.Dropdown(
                    names,
                    placeholder="Select a company",
                    className="search-bar",
                    id="dropdown",
                ),
            ],
            fluid=True,
            className="search-holder",
        )

        title = html.H1(current_name, className="company-title", id="company-title")

        self.__container.children = [title, search_holder]
