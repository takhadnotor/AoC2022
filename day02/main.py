# Please substitute "sample_input.txt" with your inputfile
with open("sample_input.txt") as file:
    lines = file.read().splitlines()

# Dictionary to get values of problem 1
# RockAX: 1, PaperBY: 2, ScissorsCZ: 3
# Lose: 0, Draw: 3, Win: 6

dictionary1 = {
    # opponent/me : status +
    "A X": 3 + 1,  # Rock/Rock
    "A Y" : 6 + 2,  # Rock/Paper
    "A Z" : 0 + 3,  # Rock/Scissors
    "B X" : 0 + 1,  # Paper/Rock
    "B Y" : 3 + 2,  # Paper/Paper
    "B Z" : 6 + 3,  # Paper/Scissors
    "C X" : 6 + 1,  # Scissors/Rock
    "C Y" : 0 + 2,  # Scissors/Paper
    "C Z" : 3 + 3  # Scissors/Scissors
}

# Dictionary to get values of problem 2
# RockAX: 1, PaperBY: 2, ScissorsCZ: 3
# Lose: 0, Draw: 3, Win: 6

dictionary2 = {
    # opponent/me : status +
    "A X": 0 + 3,  # Rock/lose
    "A Y" : 3 + 1,  # Rock/draw
    "A Z" : 6 + 2,  # Rock/win
    "B X" : 0 + 1,  # Paper/lose
    "B Y" : 3 + 2,  # Paper/draw
    "B Z" : 6 + 3,  # Paper/win
    "C X" : 0 + 2,  # Scissors/lose
    "C Y" : 3 + 3,  # Scissors/draw
    "C Z" : 6 + 1  # Scissors/win
}

# check lines with dictionaries to calculate values
count1 = 0
count2 = 0
for line in lines:
    count1 += dictionary1[line]
    count2 += dictionary2[line]

print(f"Solution 1: {count1}, Solution 2: {count2}")
