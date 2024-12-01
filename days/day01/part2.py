from days.file_reader import read

def solve():
    lines = read("day01", "input.txt")

    left,right = [],[]
    for line in lines:
        s_line = line.split("   ")
        left.append(int(s_line[0]))
        right.append(int(s_line[1]))

    left_ocurrences = {i:left.count(i) for i in left}
    right_ocurrences = {i:right.count(i) for i in right}

    sum = 0
    for k, v in left_ocurrences.items():
        if k in right_ocurrences.keys():
            sum += k * v * right_ocurrences[k]
    return sum

if __name__ == "__main__":
    print(solve())