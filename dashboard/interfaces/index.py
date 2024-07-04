from pages.index.AppLayout import AppLayout
from managers.DatabaseManager import DatabaseManager
from dash import Dash


class IApp(Dash):
    pages = []
    layout: AppLayout
    databaseManager: DatabaseManager

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def start_app(self):
        pass
