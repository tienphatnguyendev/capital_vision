import dash_bootstrap_components as dbc
from dash import dcc, callback, Input, Output, State
import plotly.graph_objects as go
from pages.utils.number.format_number import format_number
from pages.components.CustomeFigure import CustomeFigure
from interfaces.index import IApp
from pages.components.Label import Label
from pages.constants.constants import COLORS


class LineGraph(dbc.Card):
    app: IApp
    _index = 0

    def __init__(self, app, title, unit, height):
        self.app = app
        self.title_text = title
        self.unit = unit
        self.index = LineGraph._index

        self._create()
        LineGraph._index += 1

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
        figure = self._create_figure()
        self.graph = dcc.Graph(
            figure=figure,
            config=dict(displayModeBar=False),
            className="line_graph",
            style={"height": "50%", "marginTop": "10px"},
            id=f"line-graph-{self._index}",
        )

    def enable_input(self):
        @callback(
            Output(f"line-graph-{self.index}", "figure"),
            Output(f"line-value-{self.index}", "children"),
            Input(f"dropdown", "value"),
            allow_duplicate=True,
        )
        def display_data(value):
            value = self.get_latest_value()
            return self._create_figure(), value

    def get_latest_value(self):
        revenues = self.app.databaseManager.get_revenue(4)
        values = revenues["value"].tolist()[::-1]
        format_value = format_number(float(values[-1]))
        return f"{self.unit}{format_value}"

    def _create_figure(self):
        revenues = self.app.databaseManager.get_revenue(4)
        years = revenues["year"].tolist()[::-1]
        values = revenues["value"].tolist()[::-1]

        true_values = [float(value) for value in values]

        self.value.children = self.get_latest_value()

        fig = CustomeFigure()

        color = COLORS.green
        if true_values[0] > true_values[-1]:
            color = COLORS.red

        fig.add_trace(
            go.Scatter(
                x=years,
                y=true_values,
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
            transition=dict(duration=500, easing="cubic-in-out"),
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

        return fig

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
            id=f"line-value-{self._index}",
        )

    def _createLable(self):
        self.lable = Label(
            125,
            40,
            [dbc.FormText("Year: 2020"), dbc.FormText("Value: $2400.506")],
            id=f"line-label-{self._index}",
        )
