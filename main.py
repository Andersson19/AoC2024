import importlib

def run_all_solutions():
    for day in range(1,26):
        day_module = f"days.day{day:02d}"  # Format day as day01, day02, etc.

        try:
            # Dynamically import part1 and part2 modules
            part1 = importlib.import_module(f"{day_module}.part1")
            part2 = importlib.import_module(f"{day_module}.part2")

            # Print results
            stars = ""
            part1_result = part1.solve()
            part2_result = part2.solve()

            if (part1_result != "Not solved yet."):
                stars += " *"
            if (part2_result != "Not solved yet."):
                stars += "*"
            
            first_half = f"Day {day:02d} - Part 1: {part1_result} "
            second_half = f"Part 2: {part2_result}"

            result = first_half + second_half + stars
            print(result)
        except ModuleNotFoundError:
            print(f"Day {day:02d}: Not yet implemented")
        except AttributeError as e:
            print(f"Day {day:02d}: Missing 'solve' function - {e}")

if __name__ == "__main__":
    run_all_solutions()
