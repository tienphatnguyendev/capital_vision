import random
import dash_bootstrap_components as dbc
from interfaces.index import IApp
from pages.components.HistoryPriceGraph import HistoryPriceGraph
from pages.components.AssetStructureGraph import AssetStructureGraph
from pages.components.LineGraph import LineGraph

LINE_GRAPH_NAME = ["Revenue", "Gross Income", "Expenses", "Liability"]
UNIT = ["$", "$", "$", ""]
MOCK_DATA = {"year": [2019, 2020, 2021, 2022], "value": [50, 80, 40, 200]}


class FirstGraphsRow(dbc.Row):
    app: IApp

    def __init__(self, height, app):
        self.row_height = height
        self.app = app
        self.line_graph_cols = []
        self.line_graphs = []
        self.create()

        super().__init__(
            self.elements,
            className="g-1 custom_row",
        )

    def enable_input(self):
        for line_graph in self.line_graphs:
            line_graph.enable_input()

    def create(self):
        self.create_line_graphs()
        self.elements = [
            dbc.Col(
                [
                    dbc.Row(
                        [
                            self.line_graph_cols[0],
                            self.line_graph_cols[1],
                        ],
                        className="g-1",
                    ),
                    dbc.Row(
                        [
                            self.line_graph_cols[2],
                            self.line_graph_cols[3],
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
        for i in range(4):
            line_graph = LineGraph(
                self.app,
                LINE_GRAPH_NAME[i],
                UNIT[i],
                self.row_height / 2 - 0.4,
            )

            self.line_graphs.append(line_graph)
            self.line_graph_cols.append(
                dbc.Col(
                    [line_graph],
                    width=6,
                )
            )
