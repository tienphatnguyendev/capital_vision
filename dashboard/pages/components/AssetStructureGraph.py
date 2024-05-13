from dash import dcc
import plotly.express as px
import pandas as pd
from pages.components.Panel import Panel


class AssetStructureGraph(Panel):
    def __init__(self):
        self.init_graph()
        super().__init__("Asset Structure", [self.graph])

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
            marker_colors=["#1BB4FA", "#2752EE", "#2752EE", "#E44B05", "#ffffff"],
            leaf_opacity=1,
            marker=dict(line=dict(color="#ffffff", width=2)),
        )

        fig.update_traces(
            textfont=dict(
                size=25,
                color=["white", "white", "white", "white", "black"],
                family="Georgia",
            ),
        )

        fig.update_layout(showlegend=True, margin=dict(t=0, r=0, l=0, b=0))
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        fig.update_layout(height=513)
        self.fig = fig
        self.graph = dcc.Graph(
            figure=fig,
            style=dict(position="relative", bottom="45px"),
        )
