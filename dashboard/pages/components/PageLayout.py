import dash_bootstrap_components as dbc


class PageLayout(dbc.Container):
    def __init__(self, children):
        super().__init__(
            children,
            fluid=True,
            className="dbc h-95",
        )
