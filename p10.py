buildings = {
    "Block A": [100, 120, 110],
    "Block B": [200, 220, 250],
    "Block C": [80, 90, 85]
}

cost_per_unit = 5
scores = []

for name, usage in buildings.items():
    total = sum(usage)
    average = total / len(usage)
    cost = total * cost_per_unit
    change = (usage[-1] - usage[0]) / usage[0] * 100

    print("\nBuilding:", name)
    print("Total Consumption:", total)
    print("Average:", average)
    print("Cost:", cost)
    print("Percentage Change:", round(change, 2), "%")

    if average > 150:
        print("Excessive Consumption")
    else:
        print("Normal Consumption")

    scores.append((name, total))

scores.sort(key=lambda x: x[1], reverse=True)
print("\nConsumption Ranking:")
for item in scores:
    print(item[0], item[1])
