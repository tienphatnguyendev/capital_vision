import plotly.graph_objects as go
from dash import dcc, html
import dash_bootstrap_components as dbc
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

    fig.update_layout(showlegend=True, margin=dict(t=0, r=0, l=0, b=0))
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")

    return dbc.Card(
        [
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
