import plotly.graph_objects as go
from dash import dcc, html
import dash_bootstrap_components as dbc
from pages.components.curved_panel import curved_panel
import plotly.express as px


def breakdown_revenue_graph():
    df = px.data.gapminder().query("continent == 'Oceania'")
    fig = px.bar(
        df,
        x="year",
        y="pop",
        hover_data=["lifeExp", "gdpPercap"],
        color="country",
        labels={"pop": "population of Canada"},
        height=400,
    )

    fig.update_layout(showlegend=True, margin=dict(t=10, r=10, l=10, b=10))
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    fig.update_layout(height=150)

    return dbc.Card(
        [
            dbc.CardHeader("Breakdown Revenue"),
            dbc.CardBody(
                [
                    dcc.Graph(
                        figure=fig,
                        style={
                            "width": "100%",
                            "height": "100%",
                        },
                    ),
                ],
                className="full_card_body",
            ),
        ],
        color="light",
        className="box_emissions",
    )
