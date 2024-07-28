import plotly.graph_objects as go
from dash import dcc
from pages.constants.constants import COLORS
from pages.components.Panel import Panel


class BreakDownCashFlow(Panel):
    def __init__(self, height):
        self.init_graph()
        super().__init__("Cash Flow", [self.graph], height)

    def init_graph(self):
        labels = [
            "Operating Revenue1",
            "Other Revenue",
            "Total Revenue [Excluding Interest]",
            "Gross Profit",
            "Costs",
            "Operating Expenses",
            "EBIT",
            "Amortization",
            "Depreciation",
            "Net Profit After Tax Before Abs",
            "Reported NPAT",
            "Pretax Profit",
            "Net Interest Expense",
            "Tax Expense",
            "Interest Revenue",
            "Interest Expense",
            "Net Abs",
            "Operating Revenue2",
        ]

        node_indices = {
            "Operating Revenue1": 0,
            "Other Revenue": 1,
            "Total Revenue [Excluding Interest]": 2,
            "Gross Profit": 3,
            "Costs": 4,
            "Operating Expenses": 5,
            "EBIT": 6,
            "Amortization": 7,
            "Depreciation": 8,
            "Net Profit After Tax Before Abs": 9,
            "Reported NPAT": 10,
            "Pretax Profit": 11,
            "Net Interest Expense": 12,
            "Tax Expense": 13,
            "Interest Revenue": 14,
            "Interest Expense": 15,
            "Net Abs": 16,
            "Operating Revenue2": 17,
        }

        profit_color = COLORS.green
        expense_color = COLORS.red
        revenue = COLORS.medium_orange

        profit_link_color = COLORS.light_green
        expense_link_color = COLORS.light_red
        revenue_link_color = COLORS.light_orange

        node_colors = [
            revenue,
            revenue,
            revenue,
            profit_color,
            profit_color,
            expense_color,
            expense_color,
            expense_color,
            expense_color,
            profit_color,
            profit_color,
            profit_color,
            expense_color,
            expense_color,
            revenue,
            expense_color,
            profit_color,
            revenue,
        ]

        link_colors = [
            revenue_link_color,
            revenue_link_color,
            profit_link_color,
            profit_link_color,
            expense_link_color,
            revenue_link_color,
            expense_link_color,
            expense_link_color,
            expense_link_color,
            profit_link_color,
            expense_link_color,
            profit_link_color,
            expense_link_color,
            profit_link_color,
            profit_link_color,
            revenue_link_color,
            expense_link_color,
        ]

        source_indices = [
            node_indices["Operating Revenue1"],
            node_indices["Other Revenue"],
            node_indices["Total Revenue [Excluding Interest]"],
            node_indices["Total Revenue [Excluding Interest]"],
            node_indices["Gross Profit"],
            node_indices["Gross Profit"],
            node_indices["Operating Expenses"],
            node_indices["Operating Expenses"],
            node_indices["Operating Expenses"],
            node_indices["Costs"],
            node_indices["Costs"],
            node_indices["Pretax Profit"],
            node_indices["Pretax Profit"],
            node_indices["Net Profit After Tax Before Abs"],
            node_indices["Net Profit After Tax Before Abs"],
            node_indices["Net Interest Expense"],
            node_indices["Net Interest Expense"],
        ]

        target_indices = [
            node_indices["Total Revenue [Excluding Interest]"],
            node_indices["Total Revenue [Excluding Interest]"],
            node_indices["Gross Profit"],
            node_indices["Costs"],
            node_indices["Operating Expenses"],
            node_indices["Operating Revenue2"],
            node_indices["EBIT"],
            node_indices["Amortization"],
            node_indices["Depreciation"],
            node_indices["Pretax Profit"],
            node_indices["Net Interest Expense"],
            node_indices["Net Profit After Tax Before Abs"],
            node_indices["Tax Expense"],
            node_indices["Reported NPAT"],
            node_indices["Net Abs"],
            node_indices["Interest Revenue"],
            node_indices["Interest Expense"],
        ]

        values = [8, 16, 14, 10, 8, 6, 4, 2, 2, 6, 4, 4, 2, 2, 2, 2, 2]

        position_x = [
            0.02,
            0.02,
            0.15,
            0.3,
            0.3,
            0.5,
            0.98,
            0.98,
            0.98,
            0.7,
            0.98,
            0.5,
            0.5,
            0.98,
            0.98,
            0.98,
            0.98,
            0.98,
        ]

        position_y = [
            0.88,
            0.38,
            0.59,
            0.35,
            0.85,
            0.45,
            0.3,
            0.4,
            0.5,
            0.65,
            0.6,
            0.68,
            0.88,
            0.78,
            0.87,
            0.95,
            0.7,
            0.1,
        ]

        fig = go.Figure(
            data=[
                go.Sankey(
                    node=dict(
                        pad=15,
                        thickness=20,
                        label=list(node_indices.keys()),
                        color=node_colors,
                        line=dict(width=0),
                        x=position_x,
                        y=position_y,
                    ),
                    link=dict(
                        source=source_indices,
                        target=target_indices,
                        value=values,
                        label=labels,
                        color=link_colors,
                    ),
                )
            ]
        )

        fig.update_layout(
            font_size=10,
        )

        fig.update_layout(showlegend=True, margin=dict(t=0, r=0, l=0, b=0))
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")

        self.fig = fig
        self.graph = dcc.Graph(
            figure=fig, config=dict(displayModeBar=False), style=dict(height="100%")
        )
