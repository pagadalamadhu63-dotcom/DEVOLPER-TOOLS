routes = [
    ("Route A", 40, 50, 20, 10),
    ("Route B", 60, 50, 25, 12),
    ("Route C", 30, 40, 15, 8)
]

for name, passengers, capacity, time, fuel in routes:
    print("\nRoute:", name)
    print("Passengers:", passengers)

    if passengers > capacity:
        print("Status: Overloaded")
    else:
        print("Status: Normal")

    print("Fuel per passenger:", round(fuel / passengers, 2))
