# Please substitute "sample_input.txt" with your inputfile
with open("sample_input.txt") as file:
    lines = file.read().splitlines()


def create_alphabets():
    var = "a"
    alphabets = []
    # starting from the ASCII value of 'a' and keep increasing the
    # value by i.
    alphabets = [(chr(ord(var)+i)) for i in range(26)]

    # adding upper case letters
    for i in range(26):
        alphabets.append(chr(ord("A")+i))
    return alphabets


def solution1(inputfile, alphabet):
    value = 0
    for line in inputfile:
        compartment1 = line[0:(len(line)//2)]
        compartment2 = line[(len(line)//2):len(line)]
        not_found = True

        for m in range(len(compartment1)):
            if not_found == False:
                break
            for n in range(len(compartment2)):
                if not_found == False:
                    break
                elif compartment1[m] == compartment2[n]:
                    value += alphabet.index(line[m]) + 1
                    not_found = False
    return(value)


def solution2(inputfile, alphabet):
    value = 0
    for i in range(0, len(inputfile), 3):
        not_found = True
        for m in range(len(inputfile[i])):
            if not_found == False:
                break
            for n in range(len(inputfile[i + 1])):
                if not_found == False:
                    break
                for o in range(len(inputfile[i + 2])):
                    if not_found == False:
                        break
                    elif inputfile[i][m] == inputfile[i + 1][n] == inputfile[i + 2][o]:
                        not_found = False
                        value += alphabet.index(inputfile[i][m]) + 1
    return value



alphabets = create_alphabets()
print(f"Solution 1: {solution1(lines, alphabets)}")
print(f"Solution 2: {solution2(lines, alphabets)}")


