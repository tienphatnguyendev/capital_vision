from pages.components.CustomeFigure import CustomeFigure
from pages.constants.constants import Colors
from pages.components.Panel import Panel
import plotly.graph_objects as go
from dash import dcc
import pandas as pd


class DebtEquityGraph(Panel):
    def __init__(self, height):
        self.init_graph()
        super().__init__("Financial Leverage", [self.graph], height=height)
        self.fig.update_layout(showlegend=True)

    def init_graph(self):
        company_data = {
            "Year": [2019, 2020, 2021, 2022, 2023],
            "Liabilities": [1000, 1200, 1100, 1300, 1250],
            "Equity": [1500, 1600, 1700, 1650, 1800],
            "Assets": [2500, 2800, 2900, 2950, 3050],
            "ROIC": [
                10.5,
                11.0,
                10.0,
                10.8,
                11.2,
            ],
        }

        df_company = pd.DataFrame(company_data)

        sector_data = {
            "Year": [2019, 2020, 2021, 2022, 2023],
            "Liabilities": [
                1100,
                1150,
                1200,
                1250,
                1300,
            ],
            "Equity": [1600, 1650, 1700, 1750, 1800],
            "Assets": [2700, 2900, 3100, 3200, 3300],
        }

        df_sector = pd.DataFrame(sector_data)

        df_company.set_index("Year", inplace=True)
        df_sector.set_index("Year", inplace=True)

        df = pd.concat([df_company, df_sector], axis=1, keys=["Company", "Sector"])

        fig = CustomeFigure(
            layout=go.Layout(
                barmode="relative",
                yaxis2=go.layout.YAxis(
                    matches="y",
                    overlaying="y",
                    anchor="x",
                ),
                legend=dict(
                    x=1,
                    y=1,
                    font=dict(size=10),
                    orientation="h",
                ),
            )
        )

        colors = {
            "Company": {
                "Equity": Colors.medium_red,
                "Liabilities": Colors.light_red,
                "Assets": Colors.red,
            },
            "Sector": {
                "Equity": Colors.medium_green,
                "Liabilities": Colors.light_green,
                "Assets": Colors.green,
            },
        }

        for i, t in enumerate(colors):
            for j, col in enumerate(df[t].columns):
                if (df[t][col] == 0).all() or col == "ROIC":
                    continue
                fig.add_bar(
                    x=df.index,
                    y=df[t][col],
                    yaxis=f"y{i + 1}",
                    offsetgroup=str(i),
                    offset=(i - 1) * 1 / 3,
                    width=1 / 3,
                    legendgroup=t,
                    legendgrouptitle_text=t,
                    name=col,
                    marker_color=colors[t][col],
                    hovertemplate="%{y}<extra></extra>",
                )

        fig.update_xaxes(dtick=1)
        fig.update_layout(yaxis_tickformat="$")

        self.fig = fig
        self.graph = dcc.Graph(
            figure=fig, style=dict(height="100%"), config=dict(displayModeBar=False)
        )

    def update_percentage_le(self, liabilities, equities):
        for i in range(0, len(liabilities)):
            total = liabilities[i] + equities[i]
            liabilities[i] = (liabilities[i] / total) * 100
            equities[i] = (equities[i] / total) * 100
