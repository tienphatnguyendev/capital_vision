import dash_bootstrap_components as dbc
from managers.constants.index import DataKeys, StatementKeys
from pages.utils.number.format_number import format_number
from interfaces.index import IApp
from pages.home.components.HistoryPriceGraph import HistoryPriceGraph
from pages.home.components.AssetStructureGraph import AssetStructureGraph
from pages.home.components.LineGraph import LineGraph
from dash import callback, Output, Input, State


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
            className="g-2 custom_row",
        )

    def enable_callback(self):
        for line_graph in self.line_graphs:
            self.enable_line_callbacks(line_graph)

    def enable_line_callbacks(self, line_graph: LineGraph):
        graph_id_name = line_graph.graph_id_name
        value_id_name = line_graph.value_id_name

        @callback(
            Output(graph_id_name, "figure"),
            Output(value_id_name, "children"),
            Input("company-title", "children"),
        )
        def display_data(children):
            return (
                line_graph.create_figure(),
                f"{line_graph.unit}{format_number(line_graph.latest_value)}",
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
                        className="g-2",
                    ),
                    dbc.Row(
                        [
                            self.line_graph_cols[2],
                            self.line_graph_cols[3],
                        ],
                        className="g-2",
                        style=dict(paddingTop="0.8vh"),
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
            self.app, "Revenue", height, 1, DataKeys.revenue, StatementKeys.profit_loss
        )

        gross_income_line = LineGraph(
            self.app,
            "Gross Income",
            height,
            2,
            DataKeys.gross_income,
            StatementKeys.profit_loss,
        )

        expenses_line = LineGraph(
            self.app,
            "Expenses",
            height,
            3,
            DataKeys.expenses,
            StatementKeys.profit_loss,
        )

        liability_line = LineGraph(
            self.app,
            "Liability",
            height,
            4,
            DataKeys.liability,
            StatementKeys.balance_sheet,
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
