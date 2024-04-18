import dash
from dash import dash_table, dcc, callback, Output, Input, html
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px


dash.register_page(__name__, path="/")

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)

layout = dbc.Container(
    [
        dbc.Row(
            [html.Div("Update Website", className="text-primary text-center fs-3")]
        ),
        dbc.Row(
            [
                dbc.RadioItems(
                    options=[
                        {"label": x, "value": x}
                        for x in ["pop", "lifeExp", "gdpPercap"]
                    ],
                    value="lifeExp",
                    inline=True,
                    id="radio-buttons-final",
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dash_table.DataTable(
                            data=df.to_dict("records"),
                            page_size=12,
                            style_table={"overflowX": "auto"},
                        ),
                    ],
                    width=6,
                ),
                dbc.Col([dcc.Graph(figure={}, id="my-first-graph-final")], width=6),
            ]
        ),
    ],
)


@callback(
    Output(component_id="my-first-graph-final", component_property="figure"),
    Input(component_id="radio-buttons-final", component_property="value"),
)
def upgrade_graph(col_chosen):
    fig = px.histogram(df, x="continent", y=col_chosen, histfunc="avg")
    return fig
