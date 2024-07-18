from dash import Dash
import dash_bootstrap_components as dbc
from pages.chatPage.ChatPage import ChatPage
from pages.home.HomePage import HomePage
from models.FinancialMetrics import FinancialMetrics
from pages.index.AppLayout import AppLayout
import dash


class App(Dash):
    layout: AppLayout

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

        self.create_pages()

    def create_pages(self):
        self.pages = []

        home = HomePage(self)
        chat = ChatPage(self)

        dash.register_page(
            "home",
            path="/",
            layout=home.layout,
        )
        dash.register_page(
            "chat",
            path="/ChatPage",
            layout=chat.layout,
        )

        self.pages.append(home)
        self.pages.append(chat)

    def start_app(self):
        self.run_server(debug=True, dev_tools_hot_reload=True, port=8001)


app = App()
server = app.server

if __name__ == "__main__":
    app.start_app()
