import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from pages.components.sidebar import sidebar
from dash_breakpoints import WindowBreakpoints


def layout():
    return dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dash.page_container,
                            WindowBreakpoints(
                                id="breakpoints",
                                # Define the breakpoint thresholds
                                widthBreakpointThresholdsPx=[1920, 1080],
                                # And their name, note that there is one more name than breakpoint thresholds
                                widthBreakpointNames=["sm", "md", "lg"],
                            ),
                        ],
                    ),
                ]
            )
        ],
        fluid=True,
        className="dbc",
    )
