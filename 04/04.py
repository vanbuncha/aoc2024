directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]

directions_two = [
    (1, 1),
    (1, -1),
]


def check_bounds(row, col, vertical_dir, horizontal_dir, word, grid):
    for i in range(len(word)):
        next_row, next_col = row + i * vertical_dir, col + i * horizontal_dir

        if not (0 <= next_row < len(grid) and 0 <= next_col < len(grid[0])):
            return False

        if grid[next_row][next_col] != word[i]:
            return False

    return True


def find_xmas(grid):
    word = "XMAS"
    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == word[0]:
                for vertical_dir, horizontal_dir in directions:
                    if check_bounds(row, col, vertical_dir, horizontal_dir, word, grid):
                        count += 1

    return count


def check_bounds_two(row, col, direction, word, grid):
    for i in range(len(word)):
        next_row, next_col = row + i * direction[0], col + i * direction[1]

        if not (0 <= next_row < len(grid) and 0 <= next_col < len(grid[0])):
            return False

        if grid[next_row][next_col] != word[i]:
            return False

    return True


def find_x_mas_shapes(grid):
    word_forward = "MAS"
    word_backward = "SAM"
    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "A":
                diag_1_mas = check_bounds_two(
                    row - 1, col - 1, directions_two[0], word_forward, grid
                )
                diag_2_mas = check_bounds_two(
                    row - 1, col + 1, directions_two[1], word_forward, grid
                )
                diag_1_sam = check_bounds_two(
                    row - 1, col - 1, directions_two[0], word_backward, grid
                )
                diag_2_sam = check_bounds_two(
                    row - 1, col + 1, directions_two[1], word_backward, grid
                )

                if (diag_1_mas and diag_2_mas) or (diag_1_sam and diag_2_sam):
                    count += 1
                elif (diag_1_mas and diag_2_sam) or (diag_1_sam and diag_2_mas):
                    count += 1

    return count


def read_file(file_path):
    with open(file_path, "r") as file:
        grid = [line.strip() for line in file.readlines()]
    return grid


input_file = "input.txt"
print(find_xmas(read_file(input_file)))
print(find_x_mas_shapes(read_file(input_file)))
