from pages.constants.constants import COLORS
from pages.components.Panel import Panel
from dash import dcc
import plotly.graph_objects as go
import random
from pages.components.CustomeFigure import CustomeFigure


class PayoutRatioGraph(Panel):
    def __init__(self, height):
        self.init_graph()
        super().__init__("Payout Dividend", [self.graph], height)

    def init_graph(self):
        payout = random.sample(range(50, 2000), 10)
        dividend_percentages = [random.random() for _ in range(10)]

        years = []
        for i in range(10):
            years.append(2019 + i)

        fig = CustomeFigure()

        fig.add_trace(
            go.Bar(
                x=years,
                y=payout,
                name="Payout",
                marker=dict(color=COLORS.light_red),
            )
        )

        fig.add_trace(
            go.Scatter(
                x=years,
                y=dividend_percentages,
                name="Percentage",
                yaxis="y2",
                marker=dict(color=COLORS.green),
            )
        )

        fig.update_layout(
            yaxis=dict(
                side="left",
            ),
            yaxis2=dict(
                side="right",
                overlaying="y",
            ),
        )
        fig.update_xaxes(dtick=1)
        fig.update_layout(yaxis_tickformat="$")
        fig.update_layout(yaxis2_tickformat=".1%")
        fig.update_traces(
            hoverlabel=dict(
                font_size=16,
                font_family='Courier "Courier New"',
            ),
            hovertemplate="Year: <b>%{x}</b><br>Value: <b>%{y}</b>",
        )

        self.fig = fig
        self.graph = dcc.Graph(
            figure=fig, style=dict(height="100%"), config=dict(displayModeBar=False)
        )
