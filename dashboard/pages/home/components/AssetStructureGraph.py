from dash import dcc
import plotly.express as px
import pandas as pd
from pages.components.CustomeFigure import CustomeFigure
from pages.constants.constants import Colors
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
                liabilities=[None, "Short Term", "Long Term"],
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
                Colors.green,
                Colors.light_red,
                Colors.light_red,
                Colors.red,
                "#ffffff",
            ],
            leaf_opacity=1,
            marker=dict(line=dict(color="#ffffff", width=1)),
        )

        fig.update_traces(
            textfont=dict(
                color=["white", "white", "white", "white", "black"],
            ),
        )

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

        fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")

        self.graph = dcc.Graph(
            figure=fig,
            style=dict(height="100%", margin="-10px 0px 0px"),
            config=dict(displayModeBar=False),
        )
