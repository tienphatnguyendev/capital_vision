import dash_bootstrap_components as dbc


class ChatPage:
    def __init__(self, app):
        self.app = app
        self.layout = dbc.Container(
            [],
            fluid=True,
            className="dbc",
            style={"height": "95vh"},
        )
