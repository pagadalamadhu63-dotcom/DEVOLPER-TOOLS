students = ["Ravi", "Sita", "Ram", "Priya", "Ravi"]
capacity = 2
rooms = [[], []]
assigned = set()

for student in students:
    if student in assigned:
        print(student, "Duplicate assignment")
        continue

    for room in rooms:
        if len(room) < capacity:
            room.append(student)
            assigned.add(student)
            break
    else:
        print(student, "No room available")

for i, room in enumerate(rooms):
    print("Room", i + 1, ":", room)

print("Unallocated Students:", len(students) - len(assigned))
