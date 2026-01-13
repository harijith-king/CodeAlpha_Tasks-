stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}
total = 0
while True:
    name = input("Enter stock name (or done): ").upper()
    if name == "DONE":
        break

    if name not in stocks:
        print("Stock not found")
        continue

    qty = int(input("Enter quantity: "))
    total += stocks[name] * qty

print("Total Investment Value:", total)
save = input("Save result to file? (y/n): ").lower()
if save == "y":
    with open("portfolio.txt", "w") as f:
        f.write("Total Investment Value: " + str(total))
