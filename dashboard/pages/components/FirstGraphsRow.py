import dash
from dash import html
import pandas as pd
import dash_bootstrap_components as dbc
from pages.components.DupontRatiosGraph import DupontRatiosGraph
from pages.components.CashFlowGraph import CashFlowGraph
from pages.components.AssetStructureGraph import AssetStructureGraph
from pages.components.LineGraph import LineGraph

LINE_GRAPH_NAME = ["Revenue", "Gross profit", "Expenses", "Dept Ratio"]
QUOTATIONS = ["$", "$", "$", ""]
MOCK_DATA = {"year": [2019, 2020, 2021, 2022], "value": [50, 80, 40, 200]}


class FirstGraphsRow(dbc.Row):
    def __init__(self):
        self.create()

        super().__init__(
            self.elements,
            className="g-2 custom_row",
        )

    def create(self):
        self.create_line_graphs()
        self.elements = [
            dbc.Col(
                [
                    dbc.Row(
                        self.line_graphs,
                        className="g-2",
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                CashFlowGraph(),
                                width=6,
                            ),
                            dbc.Col(DupontRatiosGraph(), width=6),
                        ],
                        align="center",
                        className="g-2",
                        style={"padding": "10px 0px 0px"},
                    ),
                ],
            ),
            dbc.Col([AssetStructureGraph()], width=4),
        ]

    def create_line_graphs(self):
        self.line_graphs = []

        for i in range(4):
            data_frame = pd.DataFrame(MOCK_DATA)
            self.line_graphs.append(
                dbc.Col(
                    [
                        LineGraph(data_frame, LINE_GRAPH_NAME[i]),
                    ],
                    width=3,
                )
            )
