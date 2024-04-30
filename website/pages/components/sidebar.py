import dash
from dash import html, Input, Output, State, callback, dcc
import dash_bootstrap_components as dbc
from pages.constants.depth import DEPTH
from dash_iconify import DashIconify

SIDE_BAR_WIDTH = "210px"

COMMON_STYLE = {
    "height": "53px",
    "width": SIDE_BAR_WIDTH,
}

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


header = dbc.Container(
    [
        DashIconify(
            icon="ph:stack-light",
            style={
                "color": "#ffc336",
                "scale": "1.5",
                "margin-right": "10px",
                "margin-left": "-5px",
                "margin-top": "-5px",
            },
        ),
        html.H5(
            "Capital Vision",
            style={
                "color": "#ffffff",
                "font-size": "20px",
            },
        ),
    ],
    style={
        "display": "flex",
        "align-items": "center",
        "justify-content": "start",
        "height": "50px",
        "width": SIDE_BAR_WIDTH,
        "padding": "0 30px",
        "position": "absolute",
        "top": "35px",
    },
)


def content(icon_name, name, page_name, id):
    return dbc.NavLink(
        [
            dbc.Container(
                [
                    DashIconify(
                        icon=icon_name,
                        style=ICON_STYLE,
                    ),
                    html.P(
                        name,
                        style=TEXT_STYLE,
                    ),
                ],
                style={
                    "height": "50px",
                    "width": SIDE_BAR_WIDTH,
                    "position": "relative",
                },
            )
        ],
        id=f"sidebar-block-{id}",
        href=page_name,
        active="exact",
    )


def generate_row(content):
    return dbc.Row(
        [content],
        style=COMMON_STYLE,
    )


def sidebar():
    return dbc.Container(
        [
            dbc.Row(
                [header],
                style={
                    "width": SIDE_BAR_WIDTH,
                    "height": "95px",
                },
            ),
            generate_row(content("lucide:home", "Home", "/", 1)),
            generate_row(content("ant-design:stock-outlined", "Stock", "/stock", 2)),
            generate_row(content("mdi:about-circle-outline", "About", "/about", 3)),
        ],
        className="sidebar",
        style={
            "position": "fixed",
            "top": "0",
            "left": "0",
            "bottom": "0",
            "width": SIDE_BAR_WIDTH,
            "background-color": "#000000",
            "z-index": DEPTH["SIDE_BAR"],
        },
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
