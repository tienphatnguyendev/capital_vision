import dash_bootstrap_components as dbc


class Panel(dbc.Card):
    def __init__(
        self,
        title,
        graph,
    ):
        children = [
            dbc.CardHeader(
                title,
                className="card_header",
            ),
            dbc.CardBody(
                graph,
                className="full_card_body",
            ),
        ]

        super().__init__(
            children,
            color="light",
            className="box_emissions",
        )
