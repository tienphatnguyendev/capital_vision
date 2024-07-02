from dash.development.base_component import Component
import dash_bootstrap_components as dbc
from dash import dcc, callback, Input, Output
from pages.constants.constants import Colors


class Navbar(dbc.Row):
    def __init__(self, app, height):
        self.app = app
        self.children = []
        self.create()
        super().__init__(
            self.children,
            style=dict(
                height=f"{height}vh",
            ),
            className="custom_row",
            justify="between",
        )

    def create(self):
        self.add_company_title()
        self.add_dropdown_box()
        self.add_invest_button()

    def add_company_title(self):
        self.company_title = dbc.FormText(
            "Westpac", id="company_title", className="company_title"
        )
        self.children.append(dbc.Col([self.company_title], width=3))

    def add_dropdown_box(self):
        self.dropdown = dcc.Dropdown(
            ["New York City", "Montreal", "San Francisco"],
            placeholder="Select a company",
            className="dropdown",
            id="dropdown",
        )
        self.children.append(
            dbc.Col([self.dropdown], className="select-control-col", width=6)
        )

    def add_invest_button(self):
        self.nav_button = dbc.Button(
            "Invest Your Future",
            href="/path-to-navigate",
            className="invest_button",
            id="invest_button",
        )
        self.children.append(
            dbc.Col(
                [self.nav_button],
                width=3,
                className="nav_button_col",
            )
        )


@callback(
    Output("company_title", "children"),
    Input("dropdown", "value"),
    allow_duplicate=True,
)
def update_output(value):
    return f"{value}"
