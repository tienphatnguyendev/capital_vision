import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from pages.components.CustomeFigure import CustomeFigure


class Panel(dbc.Card):
    fig: CustomeFigure

    def __init__(self, title, graph, height=30):
        children = [
            dbc.CardHeader(
                title,
                className="card_header",
                style={"height": "20%", "borderRadius": "10px 10px 0px 0px"},
            ),
            dbc.CardBody(
                graph,
                style={
                    "height": "80%",
                    "padding": "0px 16px",
                },
                className="card_body",
            ),
        ]

        super().__init__(
            children,
            className="box_emissions bg-transparent",
            style=dict(
                height=f"{height}vh",
            ),
        )

    def update_xaxis_range(self, start, end):
        self.fig.update_xaxes(range=[start, end])
