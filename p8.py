stock = [100, 30, 80]
target = [60, 70, 80]

surplus = []
shortage = []

for i in range(len(stock)):
    difference = stock[i] - target[i]
    surplus.append(max(0, difference))
    shortage.append(max(0, -difference))

for i in range(len(stock)):
    for j in range(len(stock)):
        transfer = min(surplus[i], shortage[j])

        if i != j and transfer > 0:
            print("Transfer", transfer, "units: Branch",
                  i + 1, "to Branch", j + 1)
            surplus[i] -= transfer
            shortage[j] -= transfer
