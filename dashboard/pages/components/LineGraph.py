import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.graph_objects as go


class LineGraph(dbc.Card):
    def __init__(self, data_frame, title):
        self.data_frame = data_frame
        self.title_text = title

        self.create()

        body = dbc.CardBody(
            [self.title, self.value, self.graph],
            style={"padding-bottom": "0px"},
            className="full_card_body",
        )

        super().__init__(body, color="light", className="box_emissions")

    def create(self):
        self.create_title()
        self.create_value_text()
        self.create_graph()

    def create_graph(self):
        fig = go.Figure()

        data = self.data_frame.to_dict("list")

        x_values = data["year"]
        y_values = data["value"]

        fig.add_trace(
            go.Scatter(
                x=x_values,
                y=y_values,
                line=dict(color="#2752ee"),
                marker=dict(
                    color="#ffffff", size=5, line=dict(width=2, color="#2752ee")
                ),
            )
        )

        fig.update_xaxes(visible=False, fixedrange=True)
        fig.update_yaxes(visible=False, fixedrange=True)

        fig.update_layout(annotations=[], overwrite=True)
        fig.update_layout(showlegend=False, margin=dict(t=0, l=0, b=0, r=0))
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        fig.update_layout(height=70)

        self.fig = fig
        self.graph = dcc.Graph(
            figure=fig,
            config=dict(displayModeBar=False),
            className="line_graph",
        )

    def create_title(self):
        self.title = html.P(
            self.title_text,
            className="line_graph_text line_title",
        )

    def create_value_text(self):
        self.value = html.P(
            "$2400.50",
            className="line_graph_text line_value",
        )
