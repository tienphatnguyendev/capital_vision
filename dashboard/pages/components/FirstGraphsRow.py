import random
from dash import html, callback, Input, Output, State
import dash_bootstrap_components as dbc
from pages.components.HistoryPriceGraph import HistoryPriceGraph
from pages.components.AssetStructureGraph import AssetStructureGraph
from pages.components.LineGraph import LineGraph

LINE_GRAPH_NAME = ["Revenue", "Gross profit", "Expenses", "Dept Ratio"]
UNIT = ["$", "$", "$", ""]
MOCK_DATA = {"year": [2019, 2020, 2021, 2022], "value": [50, 80, 40, 200]}


class FirstGraphsRow(dbc.Row):
    def __init__(self, height, app):
        self.row_height = height
        self.app = app
        self.create()

        super().__init__(
            self.elements,
            className="g-1 custom_row",
        )

    def create(self):
        self.create_line_graphs()
        self.elements = [
            dbc.Col(
                [
                    dbc.Row(
                        [
                            self.line_graphs[0],
                            self.line_graphs[1],
                        ],
                        className="g-1",
                    ),
                    dbc.Row(
                        [
                            self.line_graphs[2],
                            self.line_graphs[3],
                        ],
                        className="g-1",
                        style=dict(margin="0.2vh 0vh 0vh"),
                    ),
                ],
                width=5,
            ),
            dbc.Col([AssetStructureGraph(self.row_height)], width=3),
            dbc.Col([HistoryPriceGraph(self.row_height)], width=4),
        ]

    def create_line_graphs(self):
        self.line_graphs = []

        for i in range(4):
            random_years = []

            for j in range(4):
                random_years.append(2020 + j)

            random_values = random.choices(range(50, 100), k=4)

            years = random_years
            values = random_values

            self.line_graphs.append(
                dbc.Col(
                    [
                        LineGraph(
                            years,
                            values,
                            LINE_GRAPH_NAME[i],
                            UNIT[i],
                            self.row_height / 2 - 0.4,
                        ),
                    ],
                    width=6,
                )
            )
