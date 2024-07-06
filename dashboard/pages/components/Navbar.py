from dash.development.base_component import Component
import dash_bootstrap_components as dbc
from dash import dcc, callback, Input, Output, State
from interfaces.index import IApp


class Navbar(dbc.Row):
    app: IApp

    def __init__(self, app, height):
        self.app = app
        self.children = []

        self._create()
        self._enable_input()

        super().__init__(
            self.children,
            style=dict(
                height=f"{height}vh",
            ),
            className="custom_row",
            justify="between",
        )

    def _enable_input(self):
        @callback(
            Output("company_title", "children"),
            Input("dropdown", "value"),
            State("company_title", "children"),
            allow_duplicate=True,
        )
        def update_output(value, old_value):
            if value is None:
                return old_value

            self.app.databaseManager.set_symbol(value)
            return f"{value}"

    def _create(self):
        self.add_company_title()
        self.add_dropdown_box()
        self.add_invest_button()

    def add_company_title(self):
        inital_company = self.app.databaseManager.symbol

        self.company_title = dbc.FormText(
            inital_company, id="company_title", className="company_title"
        )
        self.children.append(
            dbc.Col([self.company_title], className="select-control-col", width=3)
        )

    def add_dropdown_box(self):
        company_names = self.app.databaseManager.get_all_company_names()

        self.dropdown = dcc.Dropdown(
            company_names,
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
