stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

total = 0
portfolio = {}

print("Available stocks:", list(stocks.keys()))
budget = int(input("Enter your budget: "))

n = int(input("How many stocks you want to buy? "))

for i in range(n):
    name = input("Enter stock name: ").strip().upper()
    name = name.replace("'", "")   # handles quotes issue

    if name not in stocks:
        print("Stock not available!")
        continue

    qty = input("Enter quantity: ")

    if not qty.isdigit():
        print("Enter valid number!")
        continue

    qty = int(qty)

    amount = stocks[name] * qty
    print(name, "→", qty, "×", stocks[name], "=", amount)

    total += amount
    portfolio[name] = portfolio.get(name, 0) + qty

print("\nTotal Investment Value:", total)
print("Remaining balance:", budget - total)
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    print(stock, ":", qty)

# 🔥 File handling (saving result)
with open("result.txt", "w") as f:
    f.write("Portfolio Summary:\n")
    
    for stock, qty in portfolio.items():
        f.write(f"{stock}: {qty}\n")
    
    f.write("\nTotal Investment: " + str(total))

print("Result saved to result.txt")