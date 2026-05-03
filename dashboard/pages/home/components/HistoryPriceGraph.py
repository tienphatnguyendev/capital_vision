from interfaces.index import IDatabaseManager
from pages.constants.constants import Colors
from pages.components.Panel import Panel
from dash import dcc
import plotly.graph_objects as go
import yfinance as yf
from pages.components.CustomeFigure import CustomeFigure
from datetime import date, timedelta


class HistoryPriceGraph(Panel):
    def __init__(self, observable: IDatabaseManager, height):
        self.graph_id = "history-price-graph"
        self.current_date = date.today()
        self.previous_two_year = self.current_date - timedelta(days=2 * 365)

        observable.register_observer(self)
        self.update(observable)
        self.init_graph()

        super().__init__("History Price", [self.graph], height=height)

    def update(self, observer: IDatabaseManager):
        symbol = observer.get_current_symbol()
        ticker = symbol + ".AX"
        self.df = self.get_prices(ticker)

    def create_figure(self):
        color = Colors.medium_green
        if not self.df.empty and len(self.df["Close"]) > 0:
            if self.df["Close"].iloc[-1] < self.df["Close"].iloc[0]:
                color = Colors.medium_red

        fig = CustomeFigure(
            go.Scatter(
                x=self.df["Date"] if not self.df.empty else [],
                y=self.df["Close"] if not self.df.empty else [],
                mode="lines",
                line=dict(width=2, color=color),
                stackgroup="one",
            )
        )

        fig.update_layout(yaxis_tickformat="$.1s")
        fig.update_traces(
            hovertemplate="Date: <b>%{x}</b><br>"
            + "Price: $<b>%{y:3.s}</b><extra></extra>",
        )

        return fig

    def init_graph(self):
        self.fig = self.create_figure()
        self.graph = dcc.Graph(
            figure=self.fig,
            style=dict(height="100%"),
            config=dict(displayModeBar=False),
            id=self.graph_id,
        )

    def get_prices(self, ticker):
        df = (
            yf.Ticker(ticker)
            .history(start=self.previous_two_year, end=self.current_date)
            .reset_index()
        )
        if not df.empty:
            df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")
        return df
