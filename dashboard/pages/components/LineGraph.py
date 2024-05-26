import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.graph_objects as go
from pages.constants.constants import Colors

COLORS = Colors()


class LineGraph(dbc.Card):
    def __init__(self, data_frame, title, height):
        self.data_frame = data_frame
        self.title_text = title

        self.create()

        body = dbc.CardBody(
            [self.title, self.value, self.graph],
            style={
                "padding-bottom": "0px",
            },
            className="full_card_body full_border_card_body",
        )

        super().__init__(
            body,
            color="light",
            className="box_emissions",
            style=dict(height=f"{height}vh"),
        )

    def create(self):
        self.create_title()
        self.create_value_text()
        self.create_graph()

    def create_graph(self):
        fig = go.Figure()

        data = self.data_frame.to_dict("list")

        x_values = data["year"]
        y_values = data["value"]

        color = COLORS.green
        if y_values[-1] < y_values[0]:
            color = COLORS.red

        fig.add_trace(
            go.Scatter(
                x=x_values,
                y=y_values,
                line=dict(color=color),
                marker=dict(color="#ffffff", size=5, line=dict(width=2, color=color)),
            )
        )

        fig.update_xaxes(visible=False, fixedrange=True)
        fig.update_yaxes(visible=False, fixedrange=True)

        fig.update_layout(annotations=[], overwrite=True)
        fig.update_layout(showlegend=False, margin=dict(t=0, l=0, b=0, r=0))
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")

        self.fig = fig
        self.graph = dcc.Graph(
            figure=fig,
            config=dict(displayModeBar=False),
            className="line_graph",
            style={"height": "50%", "marginTop": "10px"},
        )

    def create_title(self):
        self.title = html.P(
            self.title_text,
            className="line_graph_text line_title",
            style={"height": "20%"},
        )

    def create_value_text(self):
        self.value = html.P(
            "$2400.50",
            className="line_graph_text line_value",
            style={"height": "30%"},
        )
