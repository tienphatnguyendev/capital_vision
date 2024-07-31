import pandas as pd
from interfaces.index import IAssetStuctureGraph
from pages.constants.constants import Colors
from pages.home.components.behaviors.FigureCreateBehavior import FigureCreateBehavior
import plotly.express as px


class NonBankingAssetBehavior(FigureCreateBehavior):
    def __init__(self, graph: IAssetStuctureGraph):
        super().__init__()
        self.graph = graph

    def create_figure(self):
        equity, short_debt, long_debt = (
            self.graph.equity.value,
            self.graph.short_debt.value,
            self.graph.long_debt.value,
        )

        df = pd.DataFrame(
            dict(
                totalValue=["Total", "Total", "Total"],
                asset=["Equity", "Liabilities", "Liabilities"],
                liabilities=[None, "Short Term", "Long Term"],
                values=[equity, short_debt, long_debt],
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
