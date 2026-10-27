seats = [[101, 102], [103, 104], [105, 106]]
registered = [101, 102, 103, 104, 105]
entered = [101, 102, 102, 105]

for ticket in entered:
    if entered.count(ticket) > 1:
        print(ticket, "Duplicate entry")
    elif ticket in registered:
        print(ticket, "Valid entry")
    else:
        print(ticket, "Invalid ticket")

print("Total Seats:", sum(len(row) for row in seats))
print("Available Seats:", sum(len(row) for row in seats) - len(set(entered)))
