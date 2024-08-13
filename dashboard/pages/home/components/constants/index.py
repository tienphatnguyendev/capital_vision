from managers.constants.index import DataKeys
from pages.constants.constants import Colors


class CashFlowKeys:
    operating_revenue = "Operating Revenue"
    other_revenue = "Other Revenue"
    total_revenue_excluding_interest = "Total Revenue [Excluding Interest]"
    gross_profit = "Gross Profit"
    costs = "Costs"
    operating_expenses = "Operating Expenses"
    ebit = "EBIT"
    amortization = "Amortization"
    depreciation = "Depreciation"
    net_profit = "Net Profit"
    reported_npat = "Reported NPAT"
    pretax_profit = "Pretax Profit"
    net_interest_expense = "Net Interest Expense"
    tax_expense = "Tax Expense"
    interest_revenue = "Interest Revenue"
    interest_expense = "Interest Expense"
    net_abs = "Net Abnormals"
    gross_operating_revenue = "Gross Operating Revenue"

    interest_income = "Interest Income"
    net_interest_income = "Net Interest Income"
    doubtful_debt_prov = "Prov. for Doubtful Debts"
    less_prov_net = "Net Int.Income Less Prov"
    non_interest_income = "Non Interest Income"
    total_operating_income = "Total Operating Income"
    non_interest_expense = "Non Interest Expense"
    tax_expense = "Tax Expense"
    abnormals = "Abnormals"
    abnormals_tax = "Abnormals Tax"


LABEL_DATA_KEYS = {
    # non-banking
    CashFlowKeys.operating_revenue: [DataKeys.operating_revenue],
    CashFlowKeys.other_revenue: [DataKeys.other_revenue],
    CashFlowKeys.gross_profit: [DataKeys.gross_income],
    CashFlowKeys.operating_expenses: [DataKeys.operating_expenses],
    CashFlowKeys.ebit: [DataKeys.ebit],
    CashFlowKeys.amortization: [DataKeys.amortization],
    CashFlowKeys.depreciation: [DataKeys.depreciation],
    CashFlowKeys.net_profit: [DataKeys.net_profit],
    CashFlowKeys.reported_npat: [DataKeys.reported_npat],
    CashFlowKeys.pretax_profit: [DataKeys.pretax_profit],
    CashFlowKeys.net_interest_expense: [DataKeys.net_interest_expense],
    CashFlowKeys.tax_expense: [DataKeys.tax_expense],
    CashFlowKeys.interest_revenue: [DataKeys.interest_revenue],
    CashFlowKeys.interest_expense: [DataKeys.interest_expense],
    CashFlowKeys.net_abs: [DataKeys.net_abs],
    CashFlowKeys.gross_operating_revenue: [DataKeys.operating_revenue],
    CashFlowKeys.total_revenue_excluding_interest: [
        DataKeys.operating_revenue,
        DataKeys.other_revenue,
    ],
    CashFlowKeys.costs: [DataKeys.pretax_profit, DataKeys.net_interest_expense],
    # banking
    CashFlowKeys.interest_income: [DataKeys.interest_income],
    CashFlowKeys.net_interest_income: [DataKeys.net_interest_income],
    CashFlowKeys.doubtful_debt_prov: [DataKeys.doubtful_debt_prov],
    CashFlowKeys.less_prov_net: [DataKeys.less_prov_net],
    CashFlowKeys.non_interest_income: [DataKeys.non_interest_income],
    CashFlowKeys.non_interest_expense: [DataKeys.non_interest_expense],
    CashFlowKeys.tax_expense: [DataKeys.tax_expense],
    CashFlowKeys.abnormals: [DataKeys.abnormals],
    CashFlowKeys.abnormals_tax: [DataKeys.abnormals_tax],
    CashFlowKeys.total_operating_income: [
        DataKeys.pretax_profit,
        DataKeys.non_interest_expense,
    ],
}


LABEL_COLORS = {
    CashFlowKeys.operating_revenue: Colors.medium_orange,
    CashFlowKeys.other_revenue: Colors.medium_orange,
    CashFlowKeys.total_revenue_excluding_interest: Colors.medium_orange,
    CashFlowKeys.gross_profit: Colors.green,
    CashFlowKeys.costs: Colors.green,
    CashFlowKeys.operating_expenses: Colors.red,
    CashFlowKeys.ebit: Colors.red,
    CashFlowKeys.amortization: Colors.red,
    CashFlowKeys.depreciation: Colors.red,
    CashFlowKeys.net_profit: Colors.green,
    CashFlowKeys.reported_npat: Colors.green,
    CashFlowKeys.pretax_profit: Colors.green,
    CashFlowKeys.net_interest_expense: Colors.red,
    CashFlowKeys.tax_expense: Colors.red,
    CashFlowKeys.interest_revenue: Colors.medium_orange,
    CashFlowKeys.interest_expense: Colors.red,
    CashFlowKeys.net_abs: Colors.green,
    CashFlowKeys.gross_operating_revenue: Colors.medium_orange,
    # banking
    CashFlowKeys.interest_income: Colors.green,
    CashFlowKeys.net_interest_income: Colors.green,
    CashFlowKeys.doubtful_debt_prov: Colors.green,
    CashFlowKeys.less_prov_net: Colors.green,
    CashFlowKeys.non_interest_income: Colors.green,
    CashFlowKeys.non_interest_expense: Colors.red,
    CashFlowKeys.tax_expense: Colors.red,
    CashFlowKeys.abnormals: Colors.green,
    CashFlowKeys.abnormals_tax: Colors.green,
    CashFlowKeys.total_operating_income: Colors.green,
}


CASH_FLOW_CONSTANTS = {
    "NON_BANKING": {
        "LABELS": [
            CashFlowKeys.other_revenue,
            CashFlowKeys.operating_revenue,
            CashFlowKeys.total_revenue_excluding_interest,
            CashFlowKeys.gross_profit,
            CashFlowKeys.costs,
            CashFlowKeys.operating_expenses,
            CashFlowKeys.pretax_profit,
            CashFlowKeys.net_interest_expense,
            CashFlowKeys.net_profit,
            CashFlowKeys.gross_operating_revenue,
            CashFlowKeys.ebit,
            CashFlowKeys.amortization,
            CashFlowKeys.depreciation,
            CashFlowKeys.reported_npat,
            CashFlowKeys.net_abs,
            CashFlowKeys.tax_expense,
            CashFlowKeys.interest_revenue,
            CashFlowKeys.interest_expense,
        ],
        "LINKS": {
            CashFlowKeys.operating_revenue: [
                CashFlowKeys.total_revenue_excluding_interest
            ],
            CashFlowKeys.other_revenue: [CashFlowKeys.total_revenue_excluding_interest],
            CashFlowKeys.total_revenue_excluding_interest: [
                CashFlowKeys.gross_profit,
                CashFlowKeys.costs,
            ],
            CashFlowKeys.gross_profit: [
                CashFlowKeys.operating_expenses,
                CashFlowKeys.gross_operating_revenue,
            ],
            CashFlowKeys.costs: [
                CashFlowKeys.pretax_profit,
                CashFlowKeys.net_interest_expense,
            ],
            CashFlowKeys.operating_expenses: [
                CashFlowKeys.ebit,
                CashFlowKeys.amortization,
                CashFlowKeys.depreciation,
            ],
            CashFlowKeys.pretax_profit: [
                CashFlowKeys.net_profit,
                CashFlowKeys.tax_expense,
            ],
            CashFlowKeys.net_interest_expense: [
                CashFlowKeys.interest_revenue,
                CashFlowKeys.interest_expense,
            ],
            CashFlowKeys.net_profit: [
                CashFlowKeys.reported_npat,
                CashFlowKeys.net_abs,
            ],
        },
    },
    "BANKING": {
        "LABELS": [
            CashFlowKeys.interest_income,
            CashFlowKeys.interest_expense,
            CashFlowKeys.net_interest_income,
            CashFlowKeys.doubtful_debt_prov,
            CashFlowKeys.less_prov_net,
            CashFlowKeys.non_interest_income,
            CashFlowKeys.total_operating_income,
            CashFlowKeys.pretax_profit,
            CashFlowKeys.non_interest_expense,
            CashFlowKeys.tax_expense,
            CashFlowKeys.net_profit,
            CashFlowKeys.net_abs,
            CashFlowKeys.reported_npat,
            CashFlowKeys.abnormals_tax,
            CashFlowKeys.abnormals,
        ],
        "LINKS": {
            CashFlowKeys.interest_income: [CashFlowKeys.net_interest_income],
            CashFlowKeys.interest_expense: [CashFlowKeys.net_interest_income],
            CashFlowKeys.net_interest_income: [CashFlowKeys.less_prov_net],
            CashFlowKeys.doubtful_debt_prov: [CashFlowKeys.less_prov_net],
            CashFlowKeys.non_interest_income: [CashFlowKeys.total_operating_income],
            CashFlowKeys.less_prov_net: [CashFlowKeys.total_operating_income],
            CashFlowKeys.total_operating_income: [
                CashFlowKeys.pretax_profit,
                CashFlowKeys.non_interest_expense,
            ],
            CashFlowKeys.pretax_profit: [
                CashFlowKeys.net_profit,
                CashFlowKeys.tax_expense,
            ],
            CashFlowKeys.net_profit: [CashFlowKeys.net_abs, CashFlowKeys.reported_npat],
            CashFlowKeys.net_abs: [CashFlowKeys.abnormals_tax, CashFlowKeys.abnormals],
        },
    },
}
