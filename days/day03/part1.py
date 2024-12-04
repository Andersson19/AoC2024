import re

def solve():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        x = [re.findall("mul\(\d+\,\d+\)",line) for line in lines]
        biboy = 0
        for line in x:
            for mul in line:
                splitted = mul.split(",")
                first = int(splitted[0][4:])
                seconde = int(splitted[1][:-1])
                biboy += first * seconde
        return biboy

if __name__ == "__main__":
    print(solve())