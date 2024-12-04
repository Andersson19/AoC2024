def solve():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        stripped = [x.strip() for x in lines]
        splitted = [[int(i) for i in line.split()] for line in stripped]
        sum_boi = 0
        for row in splitted:
            sum_boi += 1 if megaboy(row) else 0

    return sum_boi


def check_row(row):
    if inc_counter(row) < 0:
        return check_decreasing(row)
    elif inc_counter(row) > 0:
        return check_increasing(row)

def inc_counter(row):
    counter = 0 
    for i in range(len(row)-1):
        if row[i] < row[i+1]:
            counter += 1
        if row[i] > row[i+1]:
            counter -= 1
    return counter
         

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
    
def megaboy(row):
    for i in range(len(row)-1):
        if check_row(row[:i] + row[i + 1:]): return True
        
        if i == len(row)-2:
            if check_row(row[:-1]): 
                return True
    return False
    
if __name__ == "__main__":
    print(solve())