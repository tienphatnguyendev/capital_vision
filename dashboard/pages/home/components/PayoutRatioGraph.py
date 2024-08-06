from collections import defaultdict
from pages.constants.constants import Colors
from pages.components.Panel import Panel
from dash import dcc
import plotly.graph_objects as go
import random
from managers.constants.index import DataKeys, StatementKeys
from pages.components.CustomeFigure import CustomeFigure
from interfaces.index import IDataBaseManager


class PayoutRatioGraph(Panel):
    def __init__(self, observable: IDataBaseManager, height):
        self.graph_id = "payout-ratio-graph"
        
        observable.register_observer(self)
        self.update(observable)
        self.init_graph()

        super().__init__("Payout Dividend", [self.graph], height)

    def update(self, observer: IDataBaseManager):
        Y_RANGE = 5

        eps = observer.get_datas(
            data_keys=[
                DataKeys.eps,
            ],
            year_range=Y_RANGE,
            statement_key=StatementKeys.per_share_statistics,
            to_million=False,
        )

        dps = observer.get_datas(
            data_keys=[
                DataKeys.dps,
            ],
            year_range=Y_RANGE,
            statement_key=StatementKeys.per_share_statistics,
            to_million=False,
        )

        dpr = [dps[year].value / eps[year].value for year in range(0, Y_RANGE)]

        self.payout = [item.value for item in eps]
        self.dividend_percentages = dpr
        self.years = [item.year for item in eps]

    def init_graph(self):
        self.fig = self.create_figure()
        self.graph = dcc.Graph(
            figure=self.fig,
            style=dict(height="100%"),
            config=dict(displayModeBar=False),
            id=self.graph_id,
        )

    def create_figure(self):
        fig = CustomeFigure()

        fig.add_trace(
            go.Bar(
                x=self.years,
                y=self.payout,
                name="Payout",
                marker=dict(color=Colors.light_red),
            )
        )

        if not all(elem == 0 for elem in self.dividend_percentages):
            fig.add_trace(
                go.Scatter(
                    x=self.years,
                    y=self.dividend_percentages,
                    name="Percentage",
                    yaxis="y2",
                    marker=dict(color=Colors.green),
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
        return fig
