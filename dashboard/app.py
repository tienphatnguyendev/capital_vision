from dash import Dash
import dash_bootstrap_components as dbc
from pages.index.AppLayout import AppLayout


class App(Dash):
    def __init__(self):
        external_stylesheets = [dbc.themes.CERULEAN]
        super().__init__(
            __name__,
            use_pages=True,
            suppress_callback_exceptions=True,
            external_stylesheets=external_stylesheets,
        )
        self.layout = AppLayout()


app = App()
server = app.server

if __name__ == "__main__":
    app.run_server(debug=True, dev_tools_hot_reload=True, port=8001)
