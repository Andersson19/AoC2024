def isPossible(result,numbers):
    solutions = []
    solutions = addOrMultiply(result,numbers,solutions)

    for solution in solutions:
        if result == solution[0]:
            return result
    return 0

def addOrMultiply(result,numbers,solutions):
    if solutions == []:
        add_list = numbers.copy()
        first = add_list[0]
        add_list = add_list[1:]
        add_list[0] = first + add_list[0]

        mul_list = numbers.copy()
        first = mul_list[0]
        mul_list = mul_list[1:]
        mul_list[0] = first * mul_list[0]
        
        solutions.append(add_list)
        solutions.append(mul_list)
        return addOrMultiply(result,numbers,solutions)
    else:
        if len(solutions[0]) == 1:
            return solutions
        else:
            new_solutions = []

            for solution in solutions:
                add_list = solution.copy()
                first = add_list[0]
                add_list = add_list[1:]
                add_list[0] = first + add_list[0]

                mul_list = solution.copy()
                first = mul_list[0]
                mul_list = mul_list[1:]
                mul_list[0] = first * mul_list[0]
                
                new_solutions.append(add_list)
                new_solutions.append(mul_list)
                # print(new_solutions)

            return addOrMultiply(result,numbers,new_solutions)
            
"""             [1,2,3]             
            +  /      \  *
            [3,3]     [2,3]
         +  /   \ * + /   \ *
          [6]   [9]  [5]  [6]
""" 

def solve():
    lines = []
    with open("input.txt", "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    sum = 0
    for line in lines:
        splitted = line.split(":")

        result = int(splitted[0])
        numbers = splitted[1].strip().split(" ")
        numbers = [int(num) for num in numbers]

        if isPossible(result, numbers):
            sum += result

    return sum

if __name__ == "__main__":
    print(solve())