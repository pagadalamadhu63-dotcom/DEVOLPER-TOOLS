readings = [
    [40, 50, 60],
    [70, 80, 90],
    [30, 45, 55]
]

for i, row in enumerate(readings):
    avg = sum(row) / len(row)

    print("Location", i + 1)
    print("Average:", avg)
    print("Maximum:", max(row))
    print("Minimum:", min(row))

    if avg > 60:
        print("Status: High Pollution")
    else:
        print("Status: Normal")
