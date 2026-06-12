# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "AMZN": 170,
    "MSFT": 200
}

total_investment = 0

print("=== Stock Portfolio Tracker ===")

while True:
    stock_name = input("Enter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not found!")
        continue

    quantity = int(input("Enter quantity: "))

    investment = stock_prices[stock_name] * quantity
    total_investment += investment

    print(f"Investment in {stock_name}: ${investment}")

print("\n===== Portfolio Summary =====")
print(f"Total Investment Value: ${total_investment}")

# Optional: Save result to a text file
with open("portfolio_summary.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write(f"Total Investment Value: ${total_investment}\n")

print("Summary saved to portfolio_summary.txt")