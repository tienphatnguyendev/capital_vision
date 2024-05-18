from pages.components.Panel import Panel
from dash import dcc
import plotly.graph_objects as go
import yfinance as yf


class HistoryPriceGraph(Panel):
    def __init__(self, height):
        self.init_graph()
        super().__init__("History Price", [self.graph], height=height)

    def init_graph(self):
        df = self.get_mock_prices("BHP.AX")

        fig = go.Figure(
            go.Scatter(
                x=df["Date"],
                y=df["Close"],
                mode="lines",
                line=dict(width=2, color="#429f28"),
                stackgroup="one",
            )
        )

        fig.update_layout(showlegend=False, margin=dict(t=0, r=0, l=0, b=0))
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")

        self.fig = fig
        self.graph = dcc.Graph(
            figure=fig, style=dict(height="100%"), config=dict(displayModeBar=False)
        )

    def get_mock_prices(self, ticker):
        df = (
            yf.Ticker(ticker)
            .history(period="1d", start="2012-05-01", end="2023-06-01")
            .reset_index()
        )
        df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")
        return df
