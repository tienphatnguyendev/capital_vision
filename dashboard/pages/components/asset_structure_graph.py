import plotly.graph_objects as go
from dash import dcc, html
import dash_bootstrap_components as dbc
from pages.components.curved_panel import curved_panel
import plotly.express as px


def asset_structure_graph():
    data = dict(
        character=[
            "Eve",
            "Cain",
            "Seth",
            "Enos",
            "Noam",
            "Abel",
            "Awan",
            "Enoch",
            "Azura",
        ],
        parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"],
        value=[10, 14, 12, 10, 2, 6, 6, 4, 4],
    )

    fig = px.sunburst(
        data,
        names="character",
        parents="parent",
        values="value",
    )

    fig.update_layout(showlegend=True, margin=dict(t=10, r=10, l=10, b=10))
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")

    return curved_panel(
        [
            dcc.Graph(
                figure=fig,
                style={
                    "width": "100%",
                    "height": "100%",
                },
            ),
        ],
        "100%",
        "100%",
    )
