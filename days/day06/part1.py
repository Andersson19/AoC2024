

def solve():
    with open("testinput.txt") as f:
        lines = f.readlines()
        lines = [list(line.strip()) for line in lines]
    
    current_pos = (0,0)
    current_direction = '^'
    for i, line in enumerate(lines):
        for j, pos in enumerate(line):
            if pos == '^':
                current_pos = (i,j)

    while current_direction != 'DONE':
        match current_direction:
            case '^':
                next_pos = (current_pos[0]-1, [current_pos[1]])
                
    
def rotate(c):
    match c:
        case '^':
            return '>'
        case '>':
            return 'v'
        case 'v':
            return '<'
        case '<':
            return '^'

 

if __name__ == "__main__":
    print(solve())