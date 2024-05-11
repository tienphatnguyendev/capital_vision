import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd


GRAPH_WIDTH = 100
GRAPH_HEIGHT = 70


def line_graph(data_frame, graph_id, graph_value_id, name):
    fig = go.Figure()

    data = data_frame.to_dict("list")

    x_values = data["year"]
    y_values = data["value"]

    fig.add_trace(
        go.Scatter(
            x=x_values,
            y=y_values,
            line=dict(color="#2752ee"),
            marker=dict(color="#ffffff", size=5, line=dict(width=2, color="#2752ee")),
        )
    )

    fig.update_xaxes(visible=False, fixedrange=True)
    fig.update_yaxes(visible=False, fixedrange=True)

    fig.update_layout(annotations=[], overwrite=True)
    fig.update_layout(showlegend=False, margin=dict(t=0, l=0, b=0, r=0))
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    fig.update_layout(height=GRAPH_HEIGHT)

    return dbc.Card(
        [
            dbc.CardBody(
                [
                    html.P(
                        name,
                        className="line_graph_text line_title",
                    ),
                    html.P(
                        "$2400.50",
                        className="line_graph_text line_value",
                        id=graph_value_id,
                    ),
                    dcc.Graph(
                        figure=fig,
                        id=graph_id,
                        config=dict(displayModeBar=False),
                        className="line_graph",
                    ),
                ],
                className="full_card_body",
                style=dict(height=f"{155}px"),
            )
        ],
        color="light",
        className="box_emissions",
    )
