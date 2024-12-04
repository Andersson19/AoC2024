def solve():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        stripped = [x.strip() for x in lines]
        splitted = [[int(i) for i in line.split()] for line in stripped]
        #ints = [int(i) for i in splitted]
        sum_boi = 0
        for row in splitted:
            sum_boi += 1 if check_row(row) else 0
        return sum_boi

def check_row(row):
    if row[0] - row[1] > 0 and row[0] - row[1] < 4:
        # check the rest as decreasing
        return check_decreasing(row[1:])
    elif row[0] - row[1] < 0 and row[0] - row[1] > -4:
        return check_increasing(row[1:])

def check_increasing(row):
    for i in range(len(row)-1):
        if row[i]-row[i+1] > -1 or row[i]-row[i+1] < -3:
            return False
    return True

def check_decreasing(row):
    for i in range(len(row)-1):
        if row[i]-row[i+1] < 1 or row[i]-row[i+1] > 3:
            return False
    return True

if __name__ == "__main__":
    print(solve())