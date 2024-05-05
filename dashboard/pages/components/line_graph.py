import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc, html

GRAPH_WIDTH = 100
GRAPH_HEIGHT = 70


def line_graph(data_frame, graph_id, graph_value_id, name):
    fig = px.line(data_frame, x="year", y="value", markers=True)

    fig.update_xaxes(visible=False, fixedrange=True)
    fig.update_yaxes(visible=False, fixedrange=True)

    fig.update_layout(annotations=[], overwrite=True)
    fig.update_layout(showlegend=False, margin=dict(t=0, l=0, b=0, r=0))
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")

    fig.update_layout(width=GRAPH_WIDTH)
    fig.update_layout(height=GRAPH_HEIGHT)

    return dbc.Card(
        [
            dbc.CardBody(
                [
                    dcc.Graph(
                        figure=fig,
                        id=graph_id,
                    ),
                    html.P(
                        "$999",
                        className="line_graph_text",
                        id=graph_value_id,
                    ),
                    html.P(
                        name,
                        className="line_graph_text",
                    ),
                ],
                className="full_card_body",
            )
        ],
        color="light",
        className="box_emissions",
    )
