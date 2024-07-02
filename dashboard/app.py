from dash import Dash
import dash_bootstrap_components as dbc
from pages.home.HomePage import HomePage
from models.FinancialMetrics import FinancialMetrics
from pages.index.AppLayout import AppLayout


class App(Dash):
    def __init__(self):
        super().__init__(
            __name__,
            use_pages=True,
            suppress_callback_exceptions=True,
            external_stylesheets=[dbc.themes.LITERA],
        )

        self.layout = AppLayout(self)
        self.financialMetricManager = FinancialMetrics()
        self.financialMetricManager.symbol("RIO")

    def start_app(self):
        self.run_server(debug=True, dev_tools_hot_reload=True, port=8001)


app = App()
server = app.server
homePage = HomePage(app)

if __name__ == "__main__":
    app.start_app()
