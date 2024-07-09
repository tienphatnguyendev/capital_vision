import random
import dash_bootstrap_components as dbc
from pages.behaviors.GetExpenseBehavior import GetExpenseBehavior
from pages.behaviors.GetGrossIncomeBehavior import GetGrossIncomeBehavior
from pages.utils.number.format_number import format_number
from pages.behaviors.GetRevenueBehavior import GetRevenueBehavior
from interfaces.index import IApp
from pages.components.HistoryPriceGraph import HistoryPriceGraph
from pages.components.AssetStructureGraph import AssetStructureGraph
from pages.components.LineGraph import LineGraph
from dash import callback, Output, Input


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
            self.enable_line_input(line_graph)

    def enable_line_input(self, line_graph):
        index = line_graph.index

        @callback(
            Output(f"line-graph-{index}", "figure"),
            Output(f"line-value-{index}", "children"),
            Input(f"dropdown", "value"),
            allow_duplicate=True,
        )
        def display_data(value):
            return (
                line_graph.create_figure(),
                f"{line_graph.unit}{format_number(line_graph.behavior.get_latest_value())}",
            )

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
        height = self.row_height / 2 - 0.4

        revenue_line = LineGraph(
            self.app, "Revenue", "$", height, 1, GetRevenueBehavior(self.app)
        )
        gross_income_line = LineGraph(
            self.app, "Gross Income", "$", height, 2, GetGrossIncomeBehavior(self.app)
        )
        expenses_line = LineGraph(
            self.app, "Expenses", "$", height, 3, GetGrossIncomeBehavior(self.app)
        )
        liability_line = LineGraph(
            self.app, "Liability", "$", height, 4, GetRevenueBehavior(self.app)
        )

        self.line_graphs = [
            revenue_line,
            gross_income_line,
            expenses_line,
            liability_line,
        ]

        self.line_graph_cols = [
            dbc.Col([revenue_line], width=6),
            dbc.Col([gross_income_line], width=6),
            dbc.Col([expenses_line], width=6),
            dbc.Col([liability_line], width=6),
        ]
