from collections import Counter

input_file = "input.txt"
left_list = []
right_list = []
# first part

# with open(input_file, "r") as file:
#     for line in file:
#         left, right = map(int, line.split())
#         left_list.append(left)
#         right_list.append(right)


# left_list.sort()
# right_list.sort()

# total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))

# print(total_distance)

# second part
similarity = 0
total_similarity = 0
with open(input_file, "r") as file:
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

        occurence = Counter(right_list)

    for value in left_list:
        if value in right_list:
            similarity = value * occurence[value]
            # print(similarity)
            total_similarity = total_similarity + similarity

    print(total_similarity)
