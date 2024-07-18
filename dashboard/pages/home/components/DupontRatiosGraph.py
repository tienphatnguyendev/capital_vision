import plotly.graph_objects as go
from dash import dcc
from pages.components.Panel import Panel


class DupontRatiosGraph(Panel):
    def __init__(self, height):
        self.init_graph()
        super().__init__("Dupont Ratios", [self.graph], height)

    def init_graph(self):
        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=[
                    "2020-01-01",
                    "2020-04-01",
                    "2020-07-01",
                    "2021-08-16",
                ],
                y=[1000, 1500, 1700, 1000],
                xperiod="M3",
                xperiodalignment="middle",
                xhoverformat="Q%q",
                hovertemplate="%{y}%{_xother}",
            )
        )

        fig.add_trace(
            go.Scatter(
                x=[
                    "2020-01-01",
                    "2020-02-01",
                    "2020-03-01",
                    "2020-04-01",
                    "2020-05-01",
                    "2020-06-01",
                    "2020-07-01",
                    "2020-08-01",
                    "2020-09-01",
                ],
                y=[1100, 1050, 1200, 1300, 1400, 1700, 1500, 1400, 1600],
                xperiod="M1",
                xperiodalignment="middle",
                hovertemplate="%{y}%{_xother}",
            )
        )

        fig.add_trace(
            go.Scatter(
                x=[
                    "2020-01-01",
                    "2020-02-01",
                    "2020-03-01",
                    "2020-04-01",
                ],
                y=[1300, 1400, 1700, 1500],
                fill="tonexty",
            )
        )

        fig.update_layout(hovermode="x unified")

        self.fig = fig
        self.graph = dcc.Graph(figure=fig, style=dict(height="100%"))
