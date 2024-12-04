with open("input.txt", "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    def check_diag_left_to_right(lines,row,pos):
        if row == len(lines) - 1 or row == 0 or pos == 0 or pos == len(lines[0]) - 1:
            return False
        if lines[row+1][pos-1] in ['M','S']:
            if lines[row-1][pos+1] in ['M','S'] and lines[row-1][pos+1] != lines[row+1][pos-1]:
                #print(f"found diag_left_to_right at {row},{pos}")
                return True
        return False
                

    def check_diag_right_to_left(lines,row,pos):
        if row == len(lines) - 1 or row == 0 or pos == 0 or pos == len(lines[0]) - 1:
            return False
        
        if lines[row-1][pos-1] in ['M','S']:
            if lines[row+1][pos+1] in ['M','S'] and lines[row+1][pos+1] != lines[row-1][pos-1]:
                #print(f"found diag_right_to_left at {row},{pos}")
                return True

        
        return False
    

    def check_all_and_count(lines,row,pos):
        return 1 if (check_diag_right_to_left(lines,row,pos) and
        check_diag_left_to_right(lines,row,pos)) else 0

    
    tot_sum = 0
    for i,line in enumerate(lines):
        #print(f"i in enumerate: {i}")
        for j,c in enumerate(line):
            #print(f"j in enumerate: {j}")
            if c == 'A':
                tot_sum += check_all_and_count(lines,i,j)
    print(tot_sum)
    