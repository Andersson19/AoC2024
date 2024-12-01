base_path = "C:\\dev\\personal\\aoc2025\\days\\"

def read(folder, file_path: str):
    path = base_path + "\\" + folder + "\\" + file_path
    file = open(path, "r")
    lines = file.readlines()
    return [x.strip() for x in lines]
