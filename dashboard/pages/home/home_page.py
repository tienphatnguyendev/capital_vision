import dash
import dash_bootstrap_components as dbc
from dash import html
from pages.components.header_graph import header_graphs
from pages.components.dupont_ratios_graph import dupont_ratios_graph
from pages.components.sankey_graph import sankey_diagam
from pages.components.breakdown_revenue_graph import breakdown_revenue_graph
from pages.components.asset_structure_graph import asset_structure_graph

dash.register_page(__name__, path="/")

layout = dbc.Container(
    [
        dbc.Row([html.P("Navbar")], style={"height": "70px"}),
        dbc.Row(
            header_graphs(),
            className="g-2 row",
        ),
        dbc.Row(
            [
                dbc.Col(
                    asset_structure_graph(),
                ),
                dbc.Col(
                    breakdown_revenue_graph(),
                ),
            ],
            className="g-2 row",
        ),
    ],
    fluid=True,
    className="dbc",
)
