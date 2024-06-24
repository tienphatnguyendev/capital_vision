import dash_bootstrap_components as dbc
from dash import html, Output, Input, callback


class Label(dbc.Container):
    def __init__(self, width, height, children, id):
        super().__init__(
            children,
            style=dict(
                width=f"{width}px", height=f"{height}px", top="20px", left="12px"
            ),
            className="label",
            id=id,
        )
        self._width = width
        self._height = height
        self._id = id
        self.x = 0
        self.y = 0
        self.visible = True

        self.velocity = 0.2

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def kill(self):
        self.visible = False

    def revive(self):
        self.visible = True

    def enable_update(self):
        @callback(
            Output(self._id, "style"), [Input("interval-component", "n_intervals")]
        )
        def update_label(n_intervals):
            return {
                "position": "absolute",
                "left": f"{self.x}px",
                "top": f"{self.y}px",
                "visibility": "visible" if self.visible else "hidden",
                "width": f"{self._width}px",
                "height": f"{self._height}px",
            }
