import dash_bootstrap_components as dbc
from dash import dcc
import plotly.graph_objects as go
from pages.utils.number.format_long_number import format_long_number
from pages.components.CustomeFigure import CustomeFigure
from interfaces.index import IApp, IDatabaseManager, Observer
from pages.constants.constants import Colors


class LineGraph(dbc.Card, Observer):
    def __init__(self, app, title, height, index, data_key, statement_key):
        self.app: IApp = app

        self.__title_text = title
        self.unit = "$"
        self.__data_key = data_key
        self.__statement_key = statement_key

        self.graph_id_name = f"line-graph-{index}"
        self.value_id_name = f"line-value-{index}"

        self.update(self.app.databaseManager)

        self.app.databaseManager.register_observer(self)

        self.__create()

        body = dbc.CardBody(
            [
                self.title,
                self.value,
                self.graph,
            ],
            style={
                "padding-bottom": "0px",
            },
            className="card_body full_border_card_body",
        )

        super().__init__(
            body,
            className="box_emissions bg-transparent",
            style=dict(height=f"{height}vh"),
        )

    def update(self, observable: IDatabaseManager):
        datas = observable.get_datas(self.__data_key, 4, self.__statement_key)
        if not datas:
            return
        self.update_new_data(datas)

    def update_new_data(self, datas):
        self.values = []
        self.years = []

        for data in datas:
            self.values.append(data.value)
            self.years.append(data.year)

        self.latest_value = self.values[-1]

    def __create(self):
        self.__create_title()
        self.__create_value_text()
        self.__create_graph()

    def __create_graph(self):
        figure = self.create_figure()
        self.graph = dcc.Graph(
            figure=figure,
            config=dict(displayModeBar=False),
            className="line_graph",
            style={"height": "50%", "marginTop": "10px"},
            id=self.graph_id_name,
        )

    def create_figure(self):
        fig = CustomeFigure()

        values = self.values
        years = self.years

        color = Colors.green
        if values[0] > values[-1]:
            color = Colors.red

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
            + self.__title_text
            + ": "
            + self.unit
            + "<b>%{y}</b><extra></extra>",
        )

        return fig

    def __create_title(self):
        self.title = dbc.FormText(
            self.__title_text,
            className="line_graph_text line_title",
            style={"height": "20%"},
        )

    def __create_value_text(self):
        latest_value = self.latest_value

        self.value = dbc.FormText(
            f"{self.unit}{format_long_number(latest_value)}",
            className="line_graph_text line_value",
            style={"height": "30%"},
            id=self.value_id_name,
        )
