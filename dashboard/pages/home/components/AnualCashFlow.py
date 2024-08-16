from managers.constants.index import DataKeys, StatementKeys
from interfaces.index import IDatabaseManager
from pages.components.CustomeFigure import CustomeFigure
from pages.constants.constants import Colors
from pages.components.Panel import Panel
import plotly.graph_objects as go
from dash import dcc


class AnualCashFlow(Panel):
    def __init__(self, observable: IDatabaseManager, height):
        self.graph_id = "anual-cash-flow-graph"
        self.set_year_range(3)

        self.update(observable)
        observable.register_observer(self)

        self.init_graph()
        super().__init__("Anual Cash", [self.graph], height)

    def set_year_range(self, year_range):
        self.year_range = year_range

    def update(self, observable: IDatabaseManager):
        operation_cashflow = observable.get_datas(
            DataKeys.operating_cashflow, self.year_range, StatementKeys.cash_flow
        )
        investing_cashflow = observable.get_datas(
            DataKeys.investing_cashflow, self.year_range, StatementKeys.cash_flow
        )
        financing_cashflow = observable.get_datas(
            DataKeys.financing_cashflow, self.year_range, StatementKeys.cash_flow
        )

        self.years = []
        self.values = []
        self.labels = []
        self.measures = []

        for i in range(self.year_range):
            self.set_values(
                operation_cashflow[i].value,
                "Operating Cashflow",
                "relative",
                operation_cashflow[i].year,
            )
            self.set_values(
                investing_cashflow[i].value,
                "Investing Cashflow",
                "relative",
                investing_cashflow[i].year,
            )
            self.set_values(
                financing_cashflow[i].value,
                "Financing Cashflow",
                "relative",
                financing_cashflow[i].year,
            )
            self.set_values(
                None, "Net Increase in Cash", "total", operation_cashflow[i].year
            )

    def set_values(self, value, name, measure, year):
        self.values.append(value)
        self.labels.append(name)
        self.measures.append(measure)
        self.years.append(year)

    def create_figure(self):
        fig = CustomeFigure(
            go.Waterfall(
                x=[
                    self.years,
                    self.labels,
                ],
                measure=self.measures,
                y=self.values,
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
        fig.update_layout(yaxis_tickformat="$.1s")
        fig.update_xaxes(tickvals=self.labels, ticktext=self.years)

        return fig

    def init_graph(self):
        self.fig = self.create_figure()
        self.graph = dcc.Graph(
            figure=self.fig,
            style=dict(height="100%"),
            config=dict(displayModeBar=False),
            id=self.graph_id,
        )
