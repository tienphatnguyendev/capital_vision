import plotly.graph_objects as go
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd


def asset_structure_graph():
    df = pd.DataFrame(
        dict(
            totalValue=["Total", "Total", "Total"],
            asset=["Equity", "Liabilities", "Liabilities"],
            liabilities=[None, "SL", "LL"],
            values=[10, 3, 3],
        )
    )

    fig = px.sunburst(
        df,
        path=["totalValue", "asset", "liabilities"],
        values="values",
        color="liabilities",
    )

    fig.update_traces(
        marker_colors=["#1BB4FA", "#2752EE", "#2752EE", "#01295F", "#ffffff"],
        leaf_opacity=1,
    )

    fig.update_traces(
        textfont=dict(
            size=25,
            color=["white", "white", "white", "white", "black"],
            family="Georgia",
        ),
    )

    fig.update_layout(showlegend=True, margin=dict(t=0, r=0, l=0, b=0))
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")

    return dbc.Card(
        [
            dbc.CardHeader("Asset Structure", className="card_header"),
            dbc.CardBody(
                [
                    dcc.Graph(
                        figure=fig,
                        # className="center_graph",
                        style=dict(bottom="40px", position="relative"),
                    )
                ],
                className="full_card_body",
            ),
        ],
        color="light",
        className="box_emissions",
    )
