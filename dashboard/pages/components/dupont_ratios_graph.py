import plotly.graph_objects as go
from dash import dcc, html
import dash_bootstrap_components as dbc
from pages.constants.constants import SECOND_ROW_GRAPH_HEIGHT
from pages.components.curved_panel import curved_panel


def dupont_ratios_graph():
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=[
                "2020-01-01",
                "2020-04-01",
                "2020-07-01",
                "2021-08-16",
            ],
            y=[1000, 1500, 1700, 1000],
            xperiod="M3",
            xperiodalignment="middle",
            xhoverformat="Q%q",
            hovertemplate="%{y}%{_xother}",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[
                "2020-01-01",
                "2020-02-01",
                "2020-03-01",
                "2020-04-01",
                "2020-05-01",
                "2020-06-01",
                "2020-07-01",
                "2020-08-01",
                "2020-09-01",
            ],
            y=[1100, 1050, 1200, 1300, 1400, 1700, 1500, 1400, 1600],
            xperiod="M1",
            xperiodalignment="middle",
            hovertemplate="%{y}%{_xother}",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[
                "2020-01-01",
                "2020-02-01",
                "2020-03-01",
                "2020-04-01",
            ],
            y=[1300, 1400, 1700, 1500],
            fill="tonexty",
        )
    )

    fig.update_layout(showlegend=True, margin=dict(t=0, r=0, l=0, b=0))
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    fig.update_layout(hovermode="x unified")
    fig.update_layout(height=SECOND_ROW_GRAPH_HEIGHT)

    return dbc.Card(
        [
            dbc.CardHeader("Dupont Ratios Graph"),
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
