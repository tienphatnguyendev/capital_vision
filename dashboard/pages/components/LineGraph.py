import dash_bootstrap_components as dbc
from dash import dcc
import plotly.graph_objects as go
from pages.components.Label import Label
from pages.constants.constants import COLORS


class LineGraph(dbc.Card):
    _index = 0

    def __init__(self, years, values, title, unit, height):
        self.title_text = title
        self.unit = unit
        self.years = years
        self.values = values

        self._create()

        body = dbc.CardBody(
            [
                self.title,
                self.value,
                self.graph,
            ],
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

    def _create(self):
        self._create_title()
        self._create_value_text()
        self._create_graph()
        LineGraph._index += 1

    def _create_graph(self):
        fig = go.Figure()

        color = COLORS.green
        if self.values[0] < self.values[-1]:
            color = COLORS.red

        fig.add_trace(
            go.Scatter(
                x=self.years,
                y=self.values,
                line=dict(color=color),
                marker=dict(color=color, size=6),
            )
        )

        fig.update_xaxes(visible=False, fixedrange=True)
        fig.update_yaxes(visible=False, fixedrange=True)

        fig.update_layout(annotations=[], overwrite=True)
        fig.update_layout(showlegend=False, margin=dict(t=0, l=0, b=0, r=0))
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")

        fig.update_layout(
            transition=dict(duration=2000, easing="cubic-in-out"),
        )
        fig.update_traces(
            hoverlabel=dict(
                bgcolor=color,
                font_size=16,
                font_family='Courier "Courier New"',
            ),
            hovertemplate="Year: <b>%{x}</b><br>"
            + self.title_text
            + ": "
            + self.unit
            + "<b>%{y}</b><extra></extra>",
        )

        self.fig = fig
        self.graph = dcc.Graph(
            figure=fig,
            config=dict(displayModeBar=False),
            className="line_graph",
            style={"height": "50%", "marginTop": "10px"},
            id=f"line-graph-{self._index}",
        )

    def _create_title(self):
        self.title = dbc.FormText(
            self.title_text,
            className="line_graph_text line_title",
            style={"height": "20%"},
        )

    def _create_value_text(self):
        self.value = dbc.FormText(
            f"{self.unit}2400.5",
            className="line_graph_text line_value",
            style={"height": "30%"},
        )

    def _createLable(self):
        self.lable = Label(
            125,
            40,
            [dbc.FormText("Year: 2020"), dbc.FormText("Value: $2400.506")],
            id=f"line-label-{self._index}",
        )
