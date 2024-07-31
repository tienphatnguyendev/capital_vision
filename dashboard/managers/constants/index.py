class DataKeys:
    revenue = "REVENUE"
    gross_income = "GROSS_INCOME"
    expenses = "EXPENSES"
    liability = "LIABILITY"
    assets = "ASSETS"
    equity = "EQUITY"
    short_debt = "SHORT_DEBT"
    long_debt = "LONG_DEBT"


class StatementKeys:
    profit_loss = "profit_n_loss"
    balance_sheet = "balance_sheet"


BANK = {
    DataKeys.revenue: "Interest Income",
    DataKeys.gross_income: "PreTax Profit",
    DataKeys.expenses: "Interest Expense",
    DataKeys.liability: "Total Liabilities",
    DataKeys.equity: "Total Equity",
}

NON_BANK = {
    DataKeys.revenue: "Total Revenue Excluding Interest",
    DataKeys.gross_income: "EBITDA",
    DataKeys.expenses: "Operating Expenses",
    DataKeys.liability: "Total Liabilities",
    DataKeys.equity: "Total Equity",
    DataKeys.short_debt: "Short-Term Debt",
    DataKeys.long_debt: "Long-Term Debt",
}

METRICS = {
    "BANK": BANK,
    "NON_BANK": NON_BANK,
}
