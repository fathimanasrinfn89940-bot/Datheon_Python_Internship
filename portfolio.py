
import csv

current_prices = {
    "AAPL": 230.00,
    "MSFT": 420.00,
    "GOOGL": 175.00
}

portfolio = {
    "AAPL": {"buy_price": 200.00, "quantity": 5},
    "MSFT": {"buy_price": 400.00, "quantity": 2},
    "GOOGL": {"buy_price": 180.00, "quantity": 3}
}

total_invested = 0
total_market_value = 0
rows = []

print("INVESTMENT PORTFOLIO SUMMARY")

for ticker, details in portfolio.items():
    buy = details["buy_price"]
    quantity = details["quantity"]
    current = current_prices[ticker]

    invested = buy * quantity
    market_value = current * quantity
    gain = market_value - invested
    percent = (gain / invested) * 100

    total_invested += invested
    total_market_value += market_value

    print("\nStock:", ticker)
    print("Invested:", invested)
    print("Market Value:", market_value)
    print("Gain/Loss:", round(gain, 2))
    print("Gain/Loss %:", round(percent, 2), "%")

    rows.append([
        ticker, buy, current, quantity,
        invested, market_value, gain, round(percent, 2)
    ])

print("\nTotal Invested:", total_invested)
print("Total Market Value:", total_market_value)
print("Total Gain/Loss:", total_market_value - total_invested)

with open("portfolio_summary.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Ticker", "Buy Price", "Current Price", "Quantity",
        "Invested", "Market Value", "Gain/Loss", "Gain/Loss %"
    ])
    writer.writerows(rows)

print("\nCSV file created successfully!")
