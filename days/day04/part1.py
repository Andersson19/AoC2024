with open("input.txt", "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    def check_diag_left_to_right(lines,row,pos,word):
        if row > len(lines) - 4 or pos > len(lines[0])-4:
            return 0
        for i in range(1,4):
            if lines[row + i][pos +i] != word[i-1]:
                return 0
        return 1
                

    def check_diag_right_to_left(lines,row,pos,word):
        if row > len(lines) - 4 or pos < 3:
            return 0
        for i in range(1,4):
            if lines[row + i][pos -i] != word[i-1]:
                return 0
        return 1

    def check_below(lines,row,pos,word):
        if row > len(lines) - 4:
            return 0
        for i in range(1,4):
            if lines[row + i][pos] != word[i-1]:
                return 0
        return 1
    def check_horisotal(lines,row,pos,word):
        if pos > len(lines[0])-4:
            return 0
        for i in range(1,4):
            if lines[row][pos+i] != word[i-1]:
                return 0
        return 1

    def check_all_and_count(lines,row,pos,word):
        return (check_diag_right_to_left(lines,row,pos,word) +
        check_diag_left_to_right(lines,row,pos,word) +
        check_below(lines,row,pos,word) +
        check_horisotal(lines,row,pos,word))
    
    forward = "MAS"
    backward = "AMX"
    tot_sum = 0
    for i,line in enumerate(lines):
        for j,c in enumerate(line):
            if c == 'X':
                tot_sum += check_all_and_count(lines,i,j,forward)
            elif c == 'S':
                tot_sum += check_all_and_count(lines,i,j,backward)
    print(tot_sum)