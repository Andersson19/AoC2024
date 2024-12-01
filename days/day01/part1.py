import numpy as np
from days.file_reader import read
def solve():
    left,right = [],[]
    file = read("day01", "input.txt")

    for line in file:
        split_line = line.split("   ")
        left.append(int(split_line[0]))
        right.append(int(split_line[1]))

    sorted_left = sorted(left)
    sorted_right = sorted(right)

    return sum(abs(np.array(sorted_left) - np.array(sorted_right)))

if __name__ == "__main__":
    print(solve())