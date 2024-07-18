import plotly.graph_objects as go
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
from pages.components.Panel import Panel


class BreakdownRevenueGraph(Panel):
    def __init__(self, height):
        self.init_graph()
        super().__init__("Breakdown Revenue", [self.graph], height)

    def init_graph(self):
        df = px.data.gapminder().query("continent == 'Oceania'")
        fig = px.bar(
            df,
            x="year",
            y="pop",
            hover_data=["lifeExp", "gdpPercap"],
            color="country",
            labels={"pop": "population of Canada"},
        )

        fig.update_layout(showlegend=True, margin=dict(t=0, r=0, l=0, b=0))
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")

        self.fig = fig
        self.graph = dcc.Graph(figure=fig, style=dict(height="100%"))
