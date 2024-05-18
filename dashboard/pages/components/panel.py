import dash_bootstrap_components as dbc


class Panel(dbc.Card):
    def __init__(self, title, graph, height=30):
        children = [
            dbc.CardHeader(title, className="card_header", style={"height": "20%"}),
            dbc.CardBody(
                graph,
                className="full_card_body",
                style={
                    "height": "80%",
                    "padding": "0px 16px",
                },
            ),
        ]

        super().__init__(
            children,
            color="light",
            className="box_emissions",
            style=dict(
                height=f"{height}vh",
            ),
        )
