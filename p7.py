key = "ABCDAB"
answers = ["ABCCAB", "BBCDAB", "ABDDAB"]

correct = [0] * len(key)

for answer in answers:
    for i in range(len(key)):
        if answer[i] == key[i]:
            correct[i] += 1

for i in range(len(key)):
    rate = correct[i] / len(answers) * 100
    print("Question", i + 1, "Success Rate:", rate, "%")

    if rate < 50:
        print("Difficult Question")
    else:
        print("Easy Question")
