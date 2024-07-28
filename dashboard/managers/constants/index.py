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
}

NON_BANK = {
    DataKeys.revenue: "Total Revenue Excluding Interest",
    DataKeys.gross_income: "EBITDA",
    DataKeys.expenses: "Operating Expenses",
    DataKeys.liability: "Total Liabilities",
    DataKeys.assets: "total_assets",
    DataKeys.equity: "total_equity",
    DataKeys.short_debt: "short_term_debt",
    DataKeys.long_debt: "long_term_debt",
}

DATA_KEYS = {
    "BANK": BANK,
    "NON_BANK": NON_BANK,
}
