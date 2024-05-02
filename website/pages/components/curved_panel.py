import dash_bootstrap_components as dbc


def curved_panel(elements, width, height, custom_style={}):
    style = {
        "width": width,
        "height": height,
        "background-color": "#ffffff",
        "border-radius": "15px",
        "box-shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.02), 0 6px 20px 0 rgba(0, 0, 0, 0.019)",
    }

    return dbc.Container(
        elements,
        style={**style, **custom_style},
    )
