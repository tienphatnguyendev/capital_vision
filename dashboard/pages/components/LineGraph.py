import dash_bootstrap_components as dbc
from dash import dcc, callback, Input, Output
import plotly.graph_objects as go
from pages.behaviors.GetLineValueBehavior import GetLineValueBehavior
from pages.utils.number.format_number import format_number
from pages.components.CustomeFigure import CustomeFigure
from interfaces.index import IApp
from pages.constants.constants import COLORS


class LineGraph(dbc.Card):
    app: IApp
    behavior: GetLineValueBehavior

    def __init__(self, app, title, unit, height, index, behavior):
        self.app = app
        self.title_text = title
        self.unit = unit
        self.index = index
        self.behavior = behavior

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

    def _create_graph(self):
        figure = self.create_figure()
        self.graph = dcc.Graph(
            figure=figure,
            config=dict(displayModeBar=False),
            className="line_graph",
            style={"height": "50%", "marginTop": "10px"},
            id=f"line-graph-{self.index}",
        )

    def create_figure(self):
        values, years = self.behavior.get_values() or ([], [])

        fig = CustomeFigure()

        color = COLORS.green
        if values[0] > values[-1]:
            color = COLORS.red

        fig.add_trace(
            go.Scatter(
                x=years,
                y=values,
                line=dict(color=color),
                marker=dict(color=color, size=6),
            )
        )

        fig.hide_axises()
        fig.update_layout(annotations=[], overwrite=True)

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

        return fig

    def _create_title(self):
        self.title = dbc.FormText(
            self.title_text,
            className="line_graph_text line_title",
            style={"height": "20%"},
        )

    def _create_value_text(self):
        latest_value = self.behavior.get_latest_value()

        self.value = dbc.FormText(
            f"{self.unit}{format_number(latest_value)}",
            className="line_graph_text line_value",
            style={"height": "30%"},
            id=f"line-value-{self.index}",
        )
