price = 50
payment = 0


while payment < price:
    print("Amount Due:", price - payment)
    coin = int(input("Insert coin: "))
    if coin in [25, 10, 5]:
        payment += coin

if payment > price:
    change = payment - price
    print(f"Change Owed: {change}")
else:
    print("Change Owed: 0")
