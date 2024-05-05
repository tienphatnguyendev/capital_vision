import plotly.graph_objects as go
import urllib, json
from dash import dcc, html
from pages.constants.constants import SECOND_ROW_GRAPH_HEIGHT
from pages.components.curved_panel import curved_panel
import dash_bootstrap_components as dbc


def sankey_diagam():

    url = "https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json"
    response = urllib.request.urlopen(url)  # type: ignore
    data = json.loads(response.read())

    # override gray link colors with 'source' colors
    opacity = 0.4
    # change 'magenta' to its 'rgba' value to add opacity
    data["data"][0]["node"]["color"] = [
        "rgba(255,0,255, 0.8)" if color == "magenta" else color
        for color in data["data"][0]["node"]["color"]
    ]
    data["data"][0]["link"]["color"] = [
        data["data"][0]["node"]["color"][src].replace("0.8", str(opacity))
        for src in data["data"][0]["link"]["source"]
    ]

    fig = go.Figure(
        data=[
            go.Sankey(
                valueformat=".0f",
                valuesuffix="TWh",
                # Define nodes
                node=dict(
                    pad=15,
                    thickness=15,
                    line=dict(color="black", width=0.5),
                    label=data["data"][0]["node"]["label"],
                    color=data["data"][0]["node"]["color"],
                ),
                # Add links
                link=dict(
                    source=data["data"][0]["link"]["source"],
                    target=data["data"][0]["link"]["target"],
                    value=data["data"][0]["link"]["value"],
                    label=data["data"][0]["link"]["label"],
                    color=data["data"][0]["link"]["color"],
                ),
            )
        ]
    )

    fig.update_layout(showlegend=True, margin=dict(t=0, r=0, l=0, b=0))
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    fig.update_layout(height=SECOND_ROW_GRAPH_HEIGHT)

    return dbc.Card(
        [
            dbc.CardHeader("Sankey Diagram"),
            dbc.CardBody(
                [
                    dcc.Graph(
                        figure=fig,
                    ),
                ],
                className="full_card_body",
            ),
        ],
        color="light",
        className="box_emissions",
    )
