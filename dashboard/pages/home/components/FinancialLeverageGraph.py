from interfaces.index import IDatabaseManager
from pages.components.CustomeFigure import CustomeFigure
from pages.constants.constants import Colors
from pages.components.Panel import Panel
import plotly.graph_objects as go
from dash import dcc
import pandas as pd
from managers.constants.index import DataKeys, StatementKeys

EQUITY = "Equity"
LIABILITY = "Liabilities"
ASSET = "Assets"


class FinancialLeverageGraph(Panel):
    def __init__(self, observable: IDatabaseManager, height):
        self.graph_id = "financial-leverage-graph"
        self.set_year_range(5)

        self.update(observable)
        observable.register_observer(self)

        self.init_graph()

        super().__init__("Financial Leverage", [self.graph], height=height)

    def set_year_range(self, year_range):
        self.year_range = year_range

    def update(self, observer: IDatabaseManager):
        liabilities = observer.get_datas(
            DataKeys.liability, self.year_range, StatementKeys.balance_sheet
        )
        equities = observer.get_datas(
            DataKeys.equity, self.year_range, StatementKeys.balance_sheet
        )

        self.liabilities = [item.value for item in liabilities]
        self.equities = [item.value for item in equities]
        self.assets = [
            self.liabilities[i] + self.equities[i] for i in range(self.year_range)
        ]
        self.years = [item.year for item in liabilities]

    def create_figure(self):
        fig = CustomeFigure(
            layout=go.Layout(
                barmode="relative",
            )
        )

        colors = {
            EQUITY: Colors.green,
            LIABILITY: Colors.red,
            ASSET: Colors.orange,
        }

        fig.add_bar(
            x=self.years,
            y=self.equities,
            name=EQUITY,
            marker_color=colors[EQUITY],
            hovertemplate="Date: <b>%{x}</b><br>"
            + "Amount: <b>%{y}</b><extra></extra>",
        )

        fig.add_bar(
            x=self.years,
            y=self.liabilities,
            name=LIABILITY,
            marker_color=colors[LIABILITY],
            hovertemplate="Date: <b>%{x}</b><br>"
            + "Amount: <b>%{y}</b><extra></extra>",
        )

        fig.add_bar(
            x=self.years,
            y=self.assets,
            name=ASSET,
            marker_color=colors[ASSET],
            hovertemplate="Date: <b>%{x}</b><br>"
            + "Amount: <b>%{y}</b><extra></extra>",
        )

        fig.update_xaxes(dtick=1)
        fig.update_layout(yaxis_tickformat="$.2s")
        fig.update_layout(showlegend=True)

        self.fig = fig
        return fig

    def init_graph(self):
        self.create_figure()
        self.graph = dcc.Graph(
            figure=self.fig,
            style=dict(height="100%"),
            config=dict(displayModeBar=False),
            id=self.graph_id,
        )
