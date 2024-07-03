from FinancialMetrics import FinancialMetrics

metrics = [
    "Operating Expenses",
]
y_range = 5

stock = FinancialMetrics().symbol("BHP").get_fin_metrics(metrics, y_range)
print(stock.to_markdown())
