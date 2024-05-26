from pages.constants.constants import Colors
from pages.components.Panel import Panel
from dash import dcc
import plotly.graph_objects as go
import random

COLORS = Colors()


class LeverageRatioGraph(Panel):
    def __init__(self, height):
        self.init_graph()
        super().__init__("Leverage Ratio", [self.graph], height)

    def init_graph(self):
        years = []
        for i in range(10):
            years.append(2019 + i)

        total_assets = [random.randint(1000, 2000) for _ in range(9)]
        equity_capital = [random.randint(500, 1000) for _ in range(9)]
        net_profit = [random.randint(100, 500) for _ in range(9)]

        roe_percentages = [
            round((net_profit[i] / equity_capital[i]) * 100, 2) for i in range(9)
        ]

        roa_percentages = [
            round((net_profit[i] / total_assets[i]) * 100, 2) for i in range(9)
        ]

        fig = go.Figure(
            layout=dict(
                barcornerradius=6,
            )
        )

        fig.add_trace(
            go.Bar(
                x=years,
                y=total_assets,
                name="Total Assets",
                marker=dict(color=f"{COLORS.light_orange}"),
            )
        )

        fig.add_trace(
            go.Bar(
                x=years,
                y=equity_capital,
                name="Equity Capital",
                marker=dict(color=f"{COLORS.light_blue}"),
            )
        )

        fig.add_trace(
            go.Bar(
                x=years,
                y=net_profit,
                name="Net Profit",
                marker=dict(color=f"{COLORS.light_green}"),
            )
        )

        fig.add_trace(
            go.Scatter(
                x=years,
                y=roe_percentages,
                name="ROE Percentage",
                yaxis="y2",
                marker=dict(color=f"{COLORS.red}"),
            )
        )

        fig.add_trace(
            go.Scatter(
                x=years,
                y=roa_percentages,
                name="ROA Percentage",
                yaxis="y2",
                marker=dict(color=f"{COLORS.orange}"),
            )
        )

        fig.update_layout(
            yaxis=dict(
                title=dict(text="Dollars per thousand"),
                side="left",
            ),
            yaxis2=dict(
                title=dict(text="Percentage"),
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
