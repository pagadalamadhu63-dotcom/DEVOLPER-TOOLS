received = [100, 150, 200]
distributed = [60, 100, 150]
damaged = [5, 10, 15]
remaining = [35, 40, 35]

for i in range(len(received)):
    expected = received[i] - distributed[i] - damaged[i]

    print("\nLocation", i + 1)
    print("Expected Stock:", expected)

    if expected != remaining[i]:
        print("Stock Discrepancy")
    else:
        print("Stock Correct")

    print("Replenishment Needed:", max(0, 100 - remaining[i]))
