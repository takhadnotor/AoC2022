# Please substitute "sample_input.txt" with your inputfile
with open("sample_input.txt") as file:
    lines = file.read().splitlines()

datastream = ["", "", "", ""]
solution1_found = False

for i in range(len(lines[0])):
    datastream.append(lines[0][i])
    if not solution1_found or len(datastream) > 14:
        datastream.pop(0)
    # print(datastream)
    if datastream[0] != "" and len(set(datastream)) == 4:
        print(f"Solution 1: {i+1}")
        solution1_found = True
    elif solution1_found and len(datastream) >= 14 and len(set(datastream)) == 14:
        print(f"Solution 2: {i+1}")
        break
