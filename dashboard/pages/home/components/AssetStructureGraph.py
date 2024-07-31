from dash import dcc
from pages.home.components.behaviors.NonBankingAssetBehavior import (
    NonBankingAssetBehavior,
)
from managers.constants.index import DataKeys, StatementKeys
from pages.home.components.behaviors.BankingAssetBehavior import BankingAssetBehavior
from pages.home.components.behaviors.FigureCreateBehavior import FigureCreateBehavior
from interfaces.index import IAssetStuctureGraph, IDataBaseManager
from pages.components.Panel import Panel


class AssetStructureGraph(Panel, IAssetStuctureGraph):
    def __init__(self, observable: IDataBaseManager, height):
        self.behavior = FigureCreateBehavior()
        self.graph_id = "asset-structure-graph"

        self.update(observable)
        self.init_graph()

        super().__init__("Asset Structure", [self.graph], height=height)
        observable.register_observer(self)

    def update(self, observable: IDataBaseManager):
        if observable.is_banking():
            self.setBehavior(BankingAssetBehavior(self))
        else:
            self.setBehavior(NonBankingAssetBehavior(self))
            self.short_debt, self.long_debt = (
                observable.get_data(DataKeys.short_debt, StatementKeys.balance_sheet),
                observable.get_data(DataKeys.long_debt, StatementKeys.balance_sheet),
            )

        self.equity, self.liabilities = (
            observable.get_data(DataKeys.equity, StatementKeys.balance_sheet),
            observable.get_data(DataKeys.liability, StatementKeys.balance_sheet),
        )

    def setBehavior(self, behavior):
        self.behavior = behavior

    def init_graph(self):
        fig = self.behavior.create_figure()
        self.graph = dcc.Graph(
            figure=fig,
            style=dict(height="100%", margin="-10px 0px 0px"),
            config=dict(displayModeBar=False),
            id=self.graph_id,
        )
