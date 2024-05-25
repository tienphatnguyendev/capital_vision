from pages.components.Panel import Panel
import plotly.graph_objects as go
from dash import dcc
import random


class AnualCashFlow(Panel):
    def __init__(self, height):
        self.init_graph()
        super().__init__("Cash", [self.graph], height)

    def init_graph(self):
        years, labels, measures, values = self.get_random_data()

        fig = go.Figure(
            go.Waterfall(
                x=[
                    years,
                    labels,
                ],
                measure=measures,
                y=values,
                base=0,
                decreasing={"marker": {"color": "#d03d37"}},
                increasing={"marker": {"color": "#429f28"}},
                totals={
                    "marker": {
                        "color": "#ff9800",
                    }
                },
            )
        )

        fig.update_layout(showlegend=False, margin=dict(t=0, r=0, l=0, b=0))
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        fig.update_traces(connector_visible=False)
        fig.update_layout(
            waterfallgroupgap=0.05,
        )

        self.fig = fig
        self.graph = dcc.Graph(
            figure=fig, style=dict(height="100%"), config=dict(displayModeBar=False)
        )

    def get_random_data(self):
        years = []
        labels = []
        measures = []
        values = []

        for i in range(1, 11):
            for j in range(1, 5):
                years.append(f"201{i}")
                if j == 4:
                    labels.append("total")
                    measures.append("total")
                    values.append(None)
                else:
                    labels.append(f"q{j}")
                    measures.append("relative")
                    values.append(random.randint(-50, 50))

        return years, labels, measures, values
