from dash import Dash
import dash_bootstrap_components as dbc
from pages.index.index_layout import layout

external_stylesheets = [dbc.themes.CERULEAN]

app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets,
)

server = app.server
app.layout = layout


if __name__ == "__main__":
    app.run_server(debug=True, dev_tools_hot_reload=True, port=8001)
