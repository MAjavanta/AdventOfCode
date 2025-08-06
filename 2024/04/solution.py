import utils
import numpy as np


def find_lead_character(lead_char, grid):
    lead_char_cords = []
    for row_num in range(len(grid)):
        for col_num in range(len(grid[row_num])):
            if grid[row_num][col_num] == lead_char:
                lead_char_cords.append([row_num, col_num])
    return lead_char_cords


def recursive_search(cord, search_word, direction, counter, grid):
    if counter == len(search_word):
        return True
    new_cord = np.add(cord, direction).tolist()
    if not (0 <= new_cord[0] <= len(grid[0]) - 1) or not (
        0 <= new_cord[1] <= len(grid) - 1
    ):
        return False
    if grid[new_cord[0]][new_cord[1]] == search_word[counter]:
        return recursive_search(new_cord, search_word, direction, counter + 1, grid)
    else:
        return False


if __name__ == "__main__":
    input_file = utils.get_input_file_by_env("04")
    grid = []
    for line in utils.get_clean_lines(input_file):
        grid.append(list(line[0]))
    directions = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    cords = find_lead_character("X", grid)
    search_word_hits = 0
    for direction in directions:
        for cord in cords:
            if recursive_search(cord, "XMAS", direction, 1, grid):
                search_word_hits += 1
    print(search_word_hits)
