def check_level(level):
    is_increasing = all(level[i] < level[i + 1] for i in range(len(level) - 1))
    is_decreasing = all(level[i] > level[i + 1] for i in range(len(level) - 1))

    valid_range = all(
        1 <= abs(level[i] - level[i + 1]) <= 3 for i in range(len(level) - 1)
    )

    return (is_increasing or is_decreasing) and valid_range


level_file = "input.txt"

with open(level_file, "r") as file:
    levels = [list(map(int, line.split())) for line in file]
    safe_reports = sum(1 for level in levels if check_level(level))

print(safe_reports)
