from pages.components.CustomeFigure import CustomeFigure
from pages.constants.constants import Colors
from pages.components.Panel import Panel
import plotly.graph_objects as go
from dash import dcc
import random


class AnualCashFlow(Panel):
    def __init__(self, height):
        self.init_graph()
        super().__init__("Anual Cash", [self.graph], height)

    def init_graph(self):
        years, labels, measures, values = self.get_random_data()

        fig = CustomeFigure(
            go.Waterfall(
                x=[
                    years,
                    labels,
                ],
                measure=measures,
                y=values,
                base=0,
                decreasing={"marker": {"color": Colors.red}},
                increasing={"marker": {"color": Colors.green}},
                totals={
                    "marker": {
                        "color": Colors.orange,
                    }
                },
            ),
        )

        fig.update_traces(connector_visible=False)
        fig.update_layout(
            waterfallgroupgap=0.1,
        )
        fig.update_layout(yaxis_tickformat="$")
        fig.update_xaxes(tickvals=labels, ticktext=years)

        self.fig = fig
        self.graph = dcc.Graph(
            figure=fig, style=dict(height="100%"), config=dict(displayModeBar=False)
        )

    def get_random_data(self):
        labels_type = ["operate", "invest", "finance", "total"]

        years = []
        measures = []
        values = []
        labels = []

        for i in range(1, 11):
            for j in range(0, 4):
                years.append(f"201{i}")
                labels.append(labels_type[j])
                if j == 3:
                    measures.append("total")
                    values.append(None)
                else:
                    measures.append("relative")
                    values.append(
                        random.randint(
                            -10,
                            10,
                        )
                    )

        return years, labels, measures, values
