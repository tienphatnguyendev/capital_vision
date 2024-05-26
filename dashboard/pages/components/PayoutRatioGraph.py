from pages.constants.constants import Colors
from pages.components.Panel import Panel
from dash import dcc
import plotly.graph_objects as go
import random

COLORS = Colors()


class PayoutRatioGraph(Panel):
    def __init__(self, height):
        self.init_graph()
        super().__init__("Payout Ratio", [self.graph], height)

    def init_graph(self):
        payout = random.sample(range(50, 2000), 10)
        dividend_percentage = random.sample(range(0, 100), 10)

        years = []
        for i in range(10):
            years.append(2019 + i)

        fig = go.Figure(
            layout=dict(
                barcornerradius=12,
            )
        )

        fig.add_trace(
            go.Bar(
                x=years,
                y=payout,
                name="Payout Dolloars",
                marker=dict(color=COLORS.light_orange),
            )
        )

        fig.add_trace(
            go.Scatter(
                x=years,
                y=dividend_percentage,
                name="Dividend Percentage",
                yaxis="y2",
                marker=dict(color=COLORS.red),
            )
        )

        fig.update_layout(
            yaxis=dict(
                title=dict(text="Payout Dolloars"),
                side="left",
            ),
            yaxis2=dict(
                title=dict(text="Dividend Percentage"),
                side="right",
                overlaying="y",
            ),
        )

        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)

        fig.update_layout(showlegend=False, margin=dict(t=0, r=0, l=0, b=0))
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        fig.update_xaxes(dtick=1)

        self.graph = dcc.Graph(
            figure=fig, style=dict(height="100%"), config=dict(displayModeBar=False)
        )
