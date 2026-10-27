courses = [
    ("Python", "Room1", "9AM"),
    ("Maths", "Room2", "9AM"),
    ("English", "Room1", "10AM"),
    ("Web", "Room1", "9AM")
]

used = []

for course, room, period in courses:
    slot = (room, period)

    if slot in used:
        print(course, "Classroom Clash")
    else:
        print(course, "Allocated")
        used.append(slot)
