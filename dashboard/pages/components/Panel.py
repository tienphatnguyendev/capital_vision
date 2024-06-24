import dash_bootstrap_components as dbc
import plotly.graph_objects as go


class Panel(dbc.Card):
    fig: go.Figure

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
                className="full_card_body",
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

        if self.fig:
            self.fig.update_xaxes(showgrid=False)
            self.fig.update_yaxes(showgrid=False)
            self.fig.update_layout(showlegend=False, margin=dict(t=0, r=0, l=0, b=0))
            self.fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
            )

    def update_xaxis_range(self, start, end):
        self.fig.update_xaxes(range=[start, end])
