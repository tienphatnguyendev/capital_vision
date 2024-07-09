from pages.constants.constants import COLORS
from pages.components.Panel import Panel
from dash import dcc
import plotly.graph_objects as go
import random
from pages.components.CustomeFigure import CustomeFigure


class LeverageRatioGraph(Panel):
    def __init__(self, height):
        self._init_graph()
        super().__init__("Profitability", [self.graph], height)

    def _init_graph(self):
        years = []
        for i in range(10):
            years.append(2019 + i)

        total_assets = [random.randint(1000, 2000) for _ in range(9)]
        equity_capital = [random.randint(500, 1000) for _ in range(9)]
        net_profit = [random.randint(100, 500) for _ in range(9)]

        roe_percentages = [
            round((net_profit[i] / equity_capital[i]), 2) for i in range(9)
        ]

        roa_percentages = [
            round((net_profit[i] / total_assets[i]), 2) for i in range(9)
        ]

        fig = CustomeFigure()

        fig.add_trace(
            go.Bar(
                x=years,
                y=total_assets,
                name="Total Assets",
                marker=dict(color=f"{COLORS.orange}"),
                hovertemplate="Year: <b>%{x}</b><br>Asset: <b>%{y}</b>",
            )
        )

        fig.add_trace(
            go.Bar(
                x=years,
                y=equity_capital,
                name="Equity Capital",
                marker=dict(color=f"{COLORS.green}"),
                hovertemplate="Year: <b>%{x}</b><br>Equity: <b>%{y}</b>",
            )
        )

        fig.add_trace(
            go.Bar(
                x=years,
                y=net_profit,
                name="Net Profit",
                marker=dict(color=f"{COLORS.medium_green}"),
                hovertemplate="Year: <b>%{x}</b><br>Profit: <b>%{y}</b>",
            )
        )

        fig.add_trace(
            go.Scatter(
                x=years,
                y=roe_percentages,
                name="ROE Percentage",
                yaxis="y2",
                marker=dict(color=f"{COLORS.light_green}"),
                hovertemplate="Year: <b>%{x}</b><br>Value: <b>%{y}</b>",
            )
        )

        fig.add_trace(
            go.Scatter(
                x=years,
                y=roa_percentages,
                name="ROA Percentage",
                yaxis="y2",
                marker=dict(color=f"{COLORS.light_orange}"),
                hovertemplate="Year: <b>%{x}</b><br>Value: <b>%{y}</b>",
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
