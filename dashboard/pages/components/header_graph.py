import dash
import pandas as pd
import dash_bootstrap_components as dbc
from pages.components.dupont_ratios_graph import dupont_ratios_graph
from pages.components.sankey_graph import sankey_diagam
from pages.components.asset_structure_graph import asset_structure_graph
from pages.components.line_graph import line_graph

LINE_GRAPH_NAME = ["Revenue", "Gross profit", "Expenses", "Dept Ratio"]
QUOTATIONS = ["$", "$", "$", ""]
MOCK_DATA = {"year": [2019, 2020, 2021, 2022], "value": [50, 80, 40, 200]}


def header_graphs():
    lineGraphs = []
    for i in range(4):
        data_frame = pd.DataFrame(MOCK_DATA)
        lineGraphs.append(
            dbc.Col(
                [
                    line_graph(
                        data_frame,
                        f"line-graph-{i}",
                        f"line-value-{i}",
                        LINE_GRAPH_NAME[i],
                    ),
                ],
                width=3,
            )
        )

    contents = [
        dbc.Col(
            [
                dbc.Row(
                    lineGraphs,
                    className="g-2 row",
                ),
                dbc.Row(
                    [
                        dbc.Col(sankey_diagam(), width=6),
                        dbc.Col(dupont_ratios_graph(), width=6),
                    ],
                    align="center",
                    className="g-2 row",
                ),
            ],
        ),
        dbc.Col([asset_structure_graph()], width=4),
    ]

    return contents
