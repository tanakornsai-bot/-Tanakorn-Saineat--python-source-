prices = []

print("Enter prices of 6 items:")
for i in range(6):
    price = int(input(f"Item {i + 1}: "))
    prices.append(price)
 
budget = int(input("\nEnter total budget: "))

current_total = 0
bought_items = []

print()

for i in range(6):
    if current_total + prices[i] <= budget:
        print(f"Item {i + 1} = {prices[i]} -> buy")
        current_total += prices[i]
        bought_items.append(prices[i])
    else:
        print(f"Item {i + 1} = {prices[i]} -> cannot buy")

    print(f"Current total = {current_total}\n")

print(f"Bought items: {bought_items}")
print(f"Total spent: {current_total}")
print(f"Remaining budget: {budget - current_total}")