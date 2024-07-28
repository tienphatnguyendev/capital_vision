import dash
from dash import Dash
import dash_bootstrap_components as dbc
from interfaces.index import IApp
from pages.chatPage.ChatPage import ChatPage
from managers.DatabaseManager import DatabaseManager
from pages.home.HomePage import HomePage
from managers.LayoutManager import LayoutManager


class App(IApp, Dash):

    def __init__(self):
        super().__init__(
            __name__,
            use_pages=True,
            suppress_callback_exceptions=True,
            external_stylesheets=[dbc.themes.LITERA],
        )

        self.layout = LayoutManager(self)
        self.databaseManager = DatabaseManager()

        self.init_pages()

    def init_pages(self):
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
