import dash
from dash import html, Input, Output, State, callback, dcc
import dash_bootstrap_components as dbc
from pages.constants.depth import DEPTH
from dash_iconify import DashIconify
from pages.constants.constants import ELEMENT

SIDE_BAR_WIDTH = f"{ELEMENT['sideBar']['width']}px"


ICON_STYLE = {
    "position": "relative",
    "float": "left",
    "top": "20px",
    "left": "12px",
    "scale": "1",
    "color": "white",
}

TEXT_STYLE = {
    "color": "#ffffff",
    "font-size": "12px",
    "float": "left",
    "position": "relative",
    "top": "18px",
    "left": "25px",
}


header = dbc.Stack(
    [
        DashIconify(icon="ph:stack-light", style={"scale": "2"}),
        html.P("Capital Vision", className="my-auto"),
    ],
    direction="horizontal",
    gap=3,
)


def content(icon_name, name, page_name, id):
    return dbc.NavLink(
        [
            dbc.Stack(
                [
                    DashIconify(
                        icon=icon_name,
                    ),
                    html.P(
                        name,
                        className="my-auto",
                    ),
                ],
                direction="horizontal",
                gap=3,
            )
        ],
        id=f"sidebar-block-{id}",
        href=page_name,
        active="exact",
    )


def generate_row(content):
    return dbc.Row(
        [content],
        justify="center",
    )


def sidebar():
    return dbc.Container(
        [
            dbc.Row([header], align="center", className="mt-2 ml-0"),
            generate_row(content("lucide:home", "Home", "/", 1)),
            generate_row(content("ant-design:stock-outlined", "Stock", "/stock", 2)),
            generate_row(content("mdi:about-circle-outline", "About", "/about", 3)),
        ],
        className="sidebar",
    )


@callback(
    [
        Output("sidebar-block-1", "style"),
        Output("sidebar-block-2", "style"),
        Output("sidebar-block-3", "style"),
    ],
    [
        Input("sidebar-block-1", "n_clicks"),
        Input("sidebar-block-2", "n_clicks"),
        Input("sidebar-block-3", "n_clicks"),
    ],
)
def update_blocks(block1_clicks, block2_clicks, block3_clicks):
    ctx = dash.callback_context

    highlighted_style = {"opacity": 1, "transition": "opacity 0.3s"}
    blurred_style = {"opacity": 0.5, "transition": "opacity 0.3s"}

    if not ctx.triggered:
        return highlighted_style, blurred_style, blurred_style

    clicked_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if clicked_id == "sidebar-block-1":
        return (
            highlighted_style,
            blurred_style,
            blurred_style,
        )
    elif clicked_id == "sidebar-block-2":
        return (
            blurred_style,
            highlighted_style,
            blurred_style,
        )
    elif clicked_id == "sidebar-block-3":
        return (
            blurred_style,
            blurred_style,
            highlighted_style,
        )
