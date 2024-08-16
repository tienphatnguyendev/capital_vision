import plotly.graph_objects as go
from dash import dcc
from managers.constants.index import StatementKeys
from interfaces.index import IDatabaseManager
from pages.home.components.constants.index import (
    CASH_FLOW_CONSTANTS,
    LABEL_COLORS,
    LABEL_DATA_KEYS,
)
from pages.components.CustomeFigure import CustomeFigure
from pages.constants.constants import Colors
from pages.components.Panel import Panel


class BreakDownCashFlow(Panel):
    def __init__(self, observable: IDatabaseManager, height):
        self.graph_id = "cash-flow-graph"

        self.update(observable)
        self.init_graph()

        observable.register_observer(self)
        super().__init__("Cash Flow", [self.graph], height)

    def update(self, observable: IDatabaseManager):
        constants = {}

        if observable.is_banking():
            constants = CASH_FLOW_CONSTANTS["BANKING"]
        else:
            constants = CASH_FLOW_CONSTANTS["NON_BANKING"]

        labels = constants["LABELS"]
        node_colors = [LABEL_COLORS[key] for key in labels]

        sources, targets = [], []
        for key, value in constants["LINKS"].items():
            key_index = labels.index(key)
            for v in value:
                sources.append(key_index)
                targets.append(labels.index(v))

        link_colors = []
        color_map = {Colors.green: Colors.light_green, Colors.red: Colors.light_red}
        for target in targets:
            color = node_colors[target]
            link_colors.append(color_map.get(color, Colors.light_orange))

        labels_values = {
            label: sum(
                abs(observable.get_data(value, StatementKeys.profit_loss).value)
                for value in LABEL_DATA_KEYS[label]
            )
            for label in labels
        }

        self.link_values = [
            labels_values[key] if len(value) == 1 else labels_values[v]
            for key, value in constants["LINKS"].items()
            for v in value
        ]
        self.labels = labels
        self.sources = sources
        self.targets = targets
        self.node_colors = node_colors
        self.link_colors = link_colors

    def init_graph(self):
        self.fig = self.create_figure()
        self.graph = dcc.Graph(
            figure=self.fig,
            config=dict(displayModeBar=False),
            style=dict(height="100%"),
            id=self.graph_id,
        )

    def create_figure(self):
        fig = CustomeFigure(
            data=[
                go.Sankey(
                    arrangement="snap",
                    node=dict(
                        pad=15,
                        thickness=20,
                        label=self.labels,
                        color=self.node_colors,
                        line=dict(width=0),
                        align="center",
                    ),
                    link=dict(
                        source=self.sources,
                        target=self.targets,
                        value=self.link_values,
                        color=self.link_colors,
                    ),
                )
            ]
        )

        fig.update_layout(
            font_size=10,
        )

        return fig
