import re
with open("input.txt", "r") as file:
    lines = file.readlines()
    joined_lines = "".join(lines)
    x = re.findall("mul\(\d+\,\d+\)|don't\(\)|do\(\)",joined_lines)
    #print(x)
    active = True
    biboy = 0
    for line in x:
        if line == "don't()":
            active = False
        elif line == "do()":
            active = True
        else:
            if active == True:
                splitted = line.split(",")
                first = int(splitted[0][4:])
                seconde = int(splitted[1][:-1])
                biboy += first * seconde
    print(biboy)

        