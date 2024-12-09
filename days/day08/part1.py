def solve():
    with open("testinput.txt","r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        
    unique_chars = {}
    for i in range(0,len(lines)):
        for j in range(0,len(lines[0])):
            char = lines[i][j]

            if char == '.':
                continue

            if char not in unique_chars.keys():
                unique_chars[char] = [(i,j)]
            else:
                unique_chars[char].append((i,j))



    point1 = unique_chars['0'][1]
    point2 = unique_chars['0'][2]

    print(point1, point2)
    
    antinode1, antinode2 = get_delta(point1, point2)

    print(antinode1, antinode2)

    lines[antinode1[0]] = lines[antinode1[0]][:antinode1[1]] + '#' + lines[antinode1[0]][antinode1[1]+1:]
    lines[antinode2[0]] = lines[antinode2[0]][:antinode2[1]] + '#' + lines[antinode2[0]][antinode2[1]+1:]

    print_lines(lines)
    return "Not solved yet."


    
def get_delta(point1: tuple[int,int], point2: tuple[int,int]):
    diff1 = abs(point1[0] - point2[0])
    diff2 = abs(point1[1] - point2[1])

    if point1[0] < point2[0]:
        point1_x_transform = diff1 * -1
        point2_x_transform = diff1

        point1_x = point1[0] + point1_x_transform
        point2_x = point2[0] + point2_x_transform
    if point1[1] < point2[1]:
        point1_y_transform = diff2 * -1
        point2_y_transform = diff2

        point1_y = point1[1] + point1_y_transform
        point2_y = point2[1] + point2_y_transform

    return (point1_x, point1_y), (point2_x, point2_y)
    

def print_lines(lines):
    for line in lines:
        print(line)

if __name__ == "__main__":
    print(solve())