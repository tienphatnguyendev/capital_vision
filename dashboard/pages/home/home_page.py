import dash
import dash_bootstrap_components as dbc
from dash import html
from pages.components.header_graph import header_container
from pages.components.dupont_ratios_graph import dupont_ratios_graph
from pages.components.sankey_graph import sankey_diagam
from pages.components.breakdown_revenue_graph import breakdown_revenue_graph
from pages.components.asset_structure_graph import asset_structure_graph

dash.register_page(__name__, path="/")

layout = dbc.Container(
    [
        dbc.Stack(
            [
                dbc.Row(header_container(), justify="center"),
                dbc.Row(
                    [
                        dbc.Col(sankey_diagam(), width=5),
                        dbc.Col(dupont_ratios_graph(), width=5),
                    ],
                    justify="center",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            asset_structure_graph(),
                            width=5,
                        ),
                        dbc.Col(
                            breakdown_revenue_graph(),
                            width=5,
                        ),
                    ],
                    justify="center",
                    className="row-2",
                ),
            ],
            gap=2,
        ),
    ],
    fluid=True,
    className="dbc",
)
