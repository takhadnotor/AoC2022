# Please substitute "sample_input.txt" with your inputfile
with open("sample_input.txt") as file:
    lines = file.read().splitlines()


def get_campsites(l):
    def create_list(i):
        list = [i for i in range(int(i.split("-")[0]), int(i.split("-")[1]) + 1)]
        return list

    a, b = l.split(",")
    return create_list(a), create_list(b)


counter1 = 0
counter2 = 0
for line in lines:
    elf1, elf2 = get_campsites(line)
    if all([item in elf2 for item in elf1]) or all([item in elf1 for item in elf2]):
        counter1 += 1
    if any([item in elf2 for item in elf1]) or any([item in elf1 for item in elf2]):
        counter2 += 1

print(f"Solution 1: {counter1}")
print(f"Solution 2: {counter2}")
