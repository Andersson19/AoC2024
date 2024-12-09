def solve():
    with open("input.txt", "r") as file:
        lines = file.readlines()
    
    page_rules_list = [line.strip() for line in lines if "|" in line]
    updates = [line.strip().split(",") for line in lines if "|" not in line and line != '\n']

    page_rules_dict = {} 

    for page_rule in page_rules_list:
        splitted_rule = page_rule.split("|")
        X = splitted_rule[0]
        Y = splitted_rule[1]
        
        if X in page_rules_dict.keys():
            page_rules_dict[X].append(Y)
        else:
            page_rules_dict[X] = [Y]

    incorrect_updates = []
    for update in updates:
        if (not isCorrectUpdate(update, page_rules_dict)):
            incorrect_updates.append(update)
        
    sumboi = 0
    for update in incorrect_updates:

        while not isCorrectUpdate(update, page_rules_dict):
            update = swap(update, page_rules_dict)

        sumboi += getMiddleOfList(update)

    return sumboi
    
def swap(update, page_rules):
    swapped = False
    for i, value in enumerate(update):
        if value in page_rules.keys():
            for num in page_rules[value]:
                if num in update:
                    index = update.index(num)
                    if index < i:
                        swapped = True
                        update[i],update[index] = update[index],update[i]
    
    if (not swapped):
        print("we have not swapped now")
        
    return update


def isCorrectUpdate(update: list[str], page_rules_dict: dict):
    reverse = update.copy()
    reverse.reverse()
    for i in range(0,len(reverse)-1):
        if (reverse[i] in page_rules_dict.keys()):
            if (reverse[i+1] in page_rules_dict[reverse[i]]):
                return False
            
        if (reverse[i] not in page_rules_dict[reverse[i+1]]):
            return False
    return True

def getMiddleOfList(update: list[str]):
    length = len(update)

    # only odd length lists
    if(length % 2 != 0):
        return int(update[length // 2])
    else:
        print("found even numbered list!")
        
if __name__ == "__main__":
    print(solve())