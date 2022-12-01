# Please substitute "sample_input.txt" with your inputfile
with open("sample_input.txt") as file:
    lines = file.read().splitlines()

calories=0
most_calories=0
elve_number=0
cal_by_elves = []
for line in lines:
    if line != "":
        calories += int(line)
    else:
        elve_number += 1
        cal_by_elves.append(calories)
        if calories > most_calories:
            most_calories = calories
            print(f"Most calories: {most_calories} by Elve Number {elve_number}")
        calories = 0

# top three elves by calories - Part 2
cal_by_elves.sort()
cal_top = 0
for i in [-1, -2, -3]:
    cal_top += cal_by_elves[i]

print(f"Solution 1: {most_calories}")
print(f"Solution 2: {cal_top}")