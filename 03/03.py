import re

input_file = "input.txt"
pattern = r"mul\((\d+),(\d+)\)"


def find_string(file):
    total = 0
    with open(input_file, "r") as file:
        for line in file:
            matches = re.findall(pattern, line)
            total += sum([int(x) * int(y) for x, y in matches])

        # print(matches)

        print(total)
        return total


def find_string_two(file):
    total = 0
    mul_state = True
    string = ""

    with open(input_file, "r") as file:
        string = file.read()

    matches = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", string)

    for match in matches:
        if match == "do()":
            mul_state = True
        elif match == "don't()":
            mul_state = False
        elif mul_state:
            numbers = re.findall(r"\d+", match)
            total += sum([int(x) * int(y) for x, y in [numbers]])

    print(total)
    return total


find_string(input_file)
find_string_two(input_file)
