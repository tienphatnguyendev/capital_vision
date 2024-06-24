from FinancialMetrics import FinancialMetrics

metrics = [
    "net_investing_cash_flow",
    "net_financing_cash_flow",
    "net_operating_cash_flow",
    "cash_at_end_of_period",
    "cash_at_beginning_of_period",
]
y_range = 5
symbol = "WOW"

stock = FinancialMetrics().symbol("BHP").get_fin_metrics(metrics, y_range)
print(stock.to_markdown())
