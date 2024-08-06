class DataKeys:
    revenue = "REVENUE"
    gross_income = "GROSS_INCOME"
    expenses = "EXPENSES"
    liability = "LIABILITY"
    assets = "ASSETS"
    equity = "EQUITY"
    short_debt = "SHORT_DEBT"
    long_debt = "LONG_DEBT"
    operating_revenue = "OPERATING_REVENUE"
    other_revenue = "OTHER_REVENUE"
    total_revenue_excluding_interest = "TOTAL_REVENUE_EXCLUDING_INTEREST"
    operating_expenses = "OPERATING_EXPENSES"
    ebit = "EBIT"
    amortization = "AMORTIZATION"
    depreciation = "DEPRECIATION"
    net_profit = "NET_PROFIT"
    reported_npat = "REPORTED_NPAT"
    pretax_profit = "PRETAX_PROFIT"
    net_interest_expense = "NET_INTEREST_EXPENSE"
    tax_expense = "TAX_EXPENSE"
    interest_revenue = "INTEREST_REVENUE"
    interest_expense = "INTEREST_EXPENSE"
    net_abs = "NET_ABS"
    interest_income = "INTEREST_INCOME"
    net_interest_income = "NET_INTEREST_INCOME"
    doubtful_debt_prov = "DOUBTFUL_DEBT_PROV"
    less_prov_net = "LESS_PROV_NET"
    non_interest_income = "NON_INTEREST_INCOME"
    non_interest_expense = "NON_INTEREST_EXPENSE"
    abnormals = "ABNORMALS"
    abnormals_tax = "ABNORMALS_TAX"


class StatementKeys:
    profit_loss = "profit_n_loss"
    balance_sheet = "balance_sheet"


BANK = {
    DataKeys.revenue: "Interest Income",
    DataKeys.gross_income: "PreTax Profit",
    DataKeys.expenses: "Interest Expense",
    DataKeys.interest_income: "Interest Income",
    DataKeys.net_interest_income: "Net Interest Income",
    DataKeys.doubtful_debt_prov: "Prov. For Doubtful Debts",
    DataKeys.less_prov_net: "Net Int.Income Less Prov",
    DataKeys.non_interest_income: "Non Interest Income",
    DataKeys.non_interest_expense: "Non Interest Expense",
    DataKeys.abnormals: "Abnormals",
    DataKeys.abnormals_tax: "Abnormals Tax",
}

NON_BANK = {
    DataKeys.revenue: "Total Revenue Excluding Interest",
    DataKeys.gross_income: "EBITDA",
    DataKeys.expenses: "Operating Expenses",
    DataKeys.short_debt: "Short-Term Debt",
    DataKeys.long_debt: "Long-Term Debt",
    DataKeys.operating_revenue: "Operating Revenue",
    DataKeys.other_revenue: "Other Revenue",
    DataKeys.total_revenue_excluding_interest: "Total Revenue Excluding Interest",
    DataKeys.operating_expenses: "Operating Expenses",
    DataKeys.ebit: "EBIT",
    DataKeys.amortization: "Amortisation",
    DataKeys.depreciation: "Depreciation",
    DataKeys.net_interest_expense: "Net Interest Expense",
    DataKeys.interest_revenue: "Interest Revenue",
}

COMMON_KEYS = {
    DataKeys.liability: "Total Liabilities",
    DataKeys.equity: "Total Equity",
    DataKeys.interest_expense: "Interest Expense",
    DataKeys.net_abs: "Net Abnormals",
    DataKeys.pretax_profit: "PreTax Profit",
    DataKeys.tax_expense: "Tax Expense",
    DataKeys.net_profit: "Net Profit after Tax Before Abnormals",
    DataKeys.reported_npat: "Reported NPAT After Abnormals",
}

BANK.update(COMMON_KEYS)
NON_BANK.update(COMMON_KEYS)

METRICS = {
    "BANK": BANK,
    "NON_BANK": NON_BANK,
}
