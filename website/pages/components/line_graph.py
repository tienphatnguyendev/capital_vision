import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, html
import pandas as pd
import plotly.graph_objects as go

GRAPH_WIDTH = 100
GRAPH_HEIGHT = 70


def line_graph(data_frame, graph_id, graph_value_id, name):
    fig = px.line(data_frame, x="year", y="value", markers=True)
    fig.update_xaxes(visible=False, fixedrange=True)
    fig.update_yaxes(visible=False, fixedrange=True)

    fig.update_layout(annotations=[], overwrite=True)
    fig.update_layout(showlegend=False, margin=dict(t=0, l=0, b=0, r=0))
    fig.update_layout(
        width=150,
        height=60,
    )
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")

    style = {
        "display": "block",
        "background-color": "#ffffff",
        "border-radius": "15px",
        "box-shadow": "0 6px 6px 0 rgba(0, 0, 0, 0.02)",
    }

    return dbc.Container(
        [
            dcc.Graph(
                figure=fig,
                id=graph_id,
            ),
            html.P(
                "$999",
                style={
                    "color": "black",
                    "font-size": "30px",
                    "text-align": "center",
                },
                id=graph_value_id,
            ),
            html.P(
                name,
                style={
                    "color": "black",
                    "font-size": "20px",
                    "text-align": "center",
                    "margin-top": "-20px",
                },
            ),
        ],
        style=style,
    )
