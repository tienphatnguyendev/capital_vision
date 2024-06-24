from dash import dcc
import plotly.express as px
import pandas as pd
from pages.constants.constants import COLORS
from pages.components.Panel import Panel


class AssetStructureGraph(Panel):
    def __init__(self, height):
        self.init_graph()
        super().__init__("Asset Structure", [self.graph], height=height)

    def init_graph(self):
        df = pd.DataFrame(
            dict(
                totalValue=["Total", "Total", "Total"],
                asset=["Equity", "Liabilities", "Liabilities"],
                liabilities=[None, "SL", "LL"],
                values=[10, 3, 3],
            )
        )

        fig = px.sunburst(
            df,
            path=["totalValue", "asset", "liabilities"],
            values="values",
            color="liabilities",
        )

        fig.update_traces(
            marker_colors=[
                COLORS.green,
                COLORS.light_red,
                COLORS.light_red,
                COLORS.red,
                "#ffffff",
            ],
            leaf_opacity=1,
            marker=dict(line=dict(color="#ffffff", width=1)),
        )

        fig.update_traces(
            textfont=dict(
                color=["white", "white", "white", "white", "black"],
                family='Courier "Courier New"',
            ),
        )

        fig.update_layout(showlegend=True, margin=dict(t=0, r=0, l=0, b=0))
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")

        fig.update_traces(
            hoverlabel=dict(
                font_size=16,
                font_family='Courier "Courier New"',
            ),
            hovertemplate=(
                "Label: <b>%{label}</b><br>"
                "Value: <b>%{value}</b><br>"
                "Parent: <b>%{parent}</b><br>"
                "<extra></extra>"
            ),
        )

        fig.update_layout()

        self.fig = fig
        self.graph = dcc.Graph(
            figure=fig,
            style=dict(height="100%", margin="-4px 0px 0px"),
            config=dict(displayModeBar=False),
        )
