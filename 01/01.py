input_file = "input.txt"

left_list = []
right_list = []

with open(input_file, "r") as file:
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)


left_list.sort()
right_list.sort()

total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))

print(total_distance)
