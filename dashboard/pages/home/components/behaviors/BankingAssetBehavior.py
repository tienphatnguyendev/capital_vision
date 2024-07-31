import pandas as pd
from interfaces.index import IAssetStuctureGraph
from pages.constants.constants import Colors
from pages.home.components.behaviors.FigureCreateBehavior import FigureCreateBehavior
import plotly.express as px


class BankingAssetBehavior(FigureCreateBehavior):
    def __init__(self, graph: IAssetStuctureGraph):
        super().__init__()
        self.graph = graph

    def create_figure(self):
        equity, liabilities = (
            self.graph.equity.value,
            self.graph.liabilities.value,
        )

        df = pd.DataFrame(
            dict(
                totalValue=[
                    "Total",
                    "Total",
                ],
                asset=["Equity", "Liabilities"],
                values=[equity, liabilities],
            )
        )

        fig = px.sunburst(
            df,
            path=["totalValue", "asset"],
            values="values",
            color="asset",
        )

        fig.update_traces(
            marker_colors=[
                Colors.green,
                Colors.red,
                "#ffffff",
            ],
            leaf_opacity=1,
            marker=dict(line=dict(color="#ffffff", width=1)),
        )

        fig.update_traces(
            textfont=dict(
                color=["white", "white", "black"],
            ),
        )

        fig.update_traces(
            hovertemplate=(
                "Label: <b>%{label}</b><br>"
                "Value: <b>%{value:.3s}</b><br>"
                "Parent: <b>%{parent}</b><br>"
                "<extra></extra>"
            ),
        )

        fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")

        return fig
