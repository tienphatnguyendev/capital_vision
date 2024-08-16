from interfaces.index import IDatabaseManager
from pages.constants.constants import Colors
from pages.components.Panel import Panel
from dash import dcc
import plotly.graph_objects as go
from pages.components.CustomeFigure import CustomeFigure
from managers.constants.index import DataKeys, StatementKeys


class ProfitabilityGraph(Panel):
    def __init__(self, observable: IDatabaseManager, height):
        self.graph_id = "profitability-graph"
        self.set_year_range(5)

        self.update(observable)
        observable.register_observer(self)

        self._init_graph()
        super().__init__("Profitability", [self.graph], height)

    def set_year_range(self, year_range):
        self.year_range = year_range

    def update(self, observable: IDatabaseManager):
        self.total_asset = observable.get_datas(
            DataKeys.total_assets,
            self.year_range,
            StatementKeys.balance_sheet,
        )

        self.equity_capital = observable.get_datas(
            DataKeys.equity,
            self.year_range,
            StatementKeys.balance_sheet,
        )
        self.net_profit = observable.get_datas(
            DataKeys.net_profit,
            self.year_range,
            StatementKeys.profit_loss,
        )
        self.roa = observable.get_datas(
            DataKeys.roa,
            self.year_range,
            StatementKeys.ratio_analysis,
            False,
        )
        self.roe = observable.get_datas(
            DataKeys.roe,
            self.year_range,
            StatementKeys.ratio_analysis,
            False,
        )
        self.years = [item.year for item in self.total_asset]

    def _init_graph(self):
        self.create_figure()
        self.graph = dcc.Graph(
            figure=self.fig,
            style=dict(
                height="100%",
            ),
            config=dict(displayModeBar=False),
            id=self.graph_id,
        )

    def create_figure(self):
        total_asset = [item.value for item in self.total_asset]
        equity_capital = [item.value for item in self.equity_capital]
        net_profit = [item.value for item in self.net_profit]
        roa = [item.value / 100 for item in self.roa]
        roe = [item.value / 100 for item in self.roe]

        fig = CustomeFigure(layout=go.Layout(legend=dict(x=1.23, y=1)))

        fig.add_trace(
            go.Bar(
                x=self.years,
                y=total_asset,
                name="Total Assets",
                marker=dict(color=f"{Colors.orange}"),
                hovertemplate="Year: <b>%{x}</b><br>Asset: <b>%{y}</b>",
            )
        )

        fig.add_trace(
            go.Bar(
                x=self.years,
                y=equity_capital,
                name="Equity Capital",
                marker=dict(color=f"{Colors.green}"),
                hovertemplate="Year: <b>%{x}</b><br>Equity: <b>%{y}</b>",
            )
        )

        fig.add_trace(
            go.Bar(
                x=self.years,
                y=net_profit,
                name="Net Profit",
                marker=dict(color=f"{Colors.medium_green}"),
                hovertemplate="Year: <b>%{x}</b><br>Profit: <b>%{y}</b>",
            )
        )

        fig.add_trace(
            go.Scatter(
                x=self.years,
                y=roe,
                name="ROE",
                yaxis="y2",
                marker=dict(color=f"{Colors.light_green}"),
                hovertemplate="Year: <b>%{x}</b><br>Value: <b>%{y}</b>",
            )
        )

        fig.add_trace(
            go.Scatter(
                x=self.years,
                y=roa,
                name="ROA",
                yaxis="y2",
                marker=dict(color=f"{Colors.light_orange}"),
                hovertemplate="Year: <b>%{x}</b><br>Value: <b>%{y}</b>",
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
        fig.update_layout(yaxis_tickformat="$.1s")
        fig.update_layout(yaxis2_tickformat=".1%")
        fig.update_traces(
            hoverlabel=dict(
                font_size=16,
                font_family='Courier "Courier New"',
            ),
            hovertemplate="Year: <b>%{x}</b><br>Value: <b>%{y}</b>",
        )
        fig.update_layout(showlegend=True)

        self.fig = fig
        return fig
