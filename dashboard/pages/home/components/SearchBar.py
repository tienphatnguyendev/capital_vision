import dash_bootstrap_components as dbc
from dash import dcc, callback, Input, Output, html


class SearchBar(dbc.Row):
    def __init__(self, app, height):
        self.app = app
        self.children = []
        self.create()
        super().__init__(
            self.container,
            style=dict(
                height=f"{height}vh",
            ),
            className="custom_row",
        )

    def create(self):
        self.container = dbc.Container(fluid=True, className="search-bar-container")

        search_holder = dbc.Container(
            [
                dcc.Dropdown(
                    ["New York City", "Montreal", "San Francisco"],
                    placeholder="Select a company",
                    className="search-bar",
                ),
            ],
            fluid=True,
            className="search-holder",
        )

        dcc.Dropdown(
            ["New York City", "Montreal", "San Francisco"],
            placeholder="Select a company",
        )

        title = html.H1("Company Name", className="company-title")

        self.container.children = [title, search_holder]
