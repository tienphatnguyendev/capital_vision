import dash
import dash_bootstrap_components as dbc


class AppLayout(dbc.Container):
    def __init__(self):
        self.create()
        super().__init__(
            self.elements,
            fluid=True,
            className="dbc",
        )

    def create(self):
        self.elements = [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dash.page_container,
                        ],
                        style={"padding": "0px"},
                    ),
                ]
            )
        ]
