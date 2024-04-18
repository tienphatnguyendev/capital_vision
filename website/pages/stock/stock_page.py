import dash
from dash import html

dash.register_page(__name__, path="/stock")


layout = html.Div("Stock Page")

