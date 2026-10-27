balance = 1000
transactions = ["deposit 500", "withdraw 200",
                "withdraw 300", "withdraw 200"]

withdrawals = 0

for transaction in transactions:
    action, amount = transaction.split()
    amount = int(amount)

    if amount <= 0:
        print("Invalid amount")
    elif action == "deposit":
        balance += amount
        withdrawals = 0
    elif action == "withdraw":
        if amount <= balance:
            balance -= amount
            withdrawals += 1
            if withdrawals >= 3:
                print("Suspicious repeated withdrawals")
        else:
            print("Insufficient balance")

print("Final Balance:", balance)
