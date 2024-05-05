import dash
from dash import dash_table, dcc, callback, Output, Input, html, Patch
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px
from pages.components.line_graph import line_graph
from pages.utils.number.format_number import format_number
import plotly.graph_objs as go

LINE_GRAPH_NAME = ["Revenue", "Gross profit", "Expenses", "Dept Ratio"]
QUOTATIONS = ["$", "$", "$", ""]
MOCK_DATA = {"year": [2019, 2020, 2021, 2022], "value": [50, 40, 45, 55]}


column_elements = []
for i in range(4):
    data_frame = pd.DataFrame(MOCK_DATA)
    column_elements.append(
        dbc.Col(
            [
                line_graph(
                    data_frame,
                    f"line-graph-{i}",
                    f"line-value-{i}",
                    LINE_GRAPH_NAME[i],
                ),
            ]
        )
    )


def header_container():
    return dbc.Container(
        [dbc.Row(column_elements)],
    )


for i in range(4):

    @callback(
        Output(f"line-value-{i}", "children"),
        Input(f"line-graph-{i}", "clickData"),
    )
    def update_line_graph(click_data, i=i):
        quotation = QUOTATIONS[i]
        value = click_data["points"][0]["y"] if click_data else MOCK_DATA["value"][0]
        format_value = format_number(value)
        return f"{quotation}{format_value}"

    @callback(
        Output(f"line-graph-{i}", "figure"),
        [Input(f"line-graph-{i}", "clickData")],
    )
    def update_graph(clicked_data, i=i):
        data_length = len(MOCK_DATA["year"])

        idx = clicked_data["points"][0]["pointIndex"] if clicked_data else 0

        marker_colors = ["grey"] * data_length
        marker_sizes = [8] * data_length
        marker_opacity = [0.5] * data_length

        marker_opacity[idx] = 1
        marker_colors[idx] = "red"
        marker_sizes[idx] = 12

        patched_figure = Patch()
        patched_figure["data"][0]["marker"] = dict(
            color=marker_colors, size=marker_sizes, opacity=marker_opacity
        )
        patched_figure["data"][0]["line"] = dict(color="black")
        return patched_figure
