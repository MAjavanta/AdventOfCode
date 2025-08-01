from dotenv import load_dotenv
import os


load_dotenv()


def get_file_lines(input_file):
    with open(input_file, "r") as f:
        lines = []
        for line in f:
            lines.append([char for char in line.strip().split()])
    return lines


def get_env():
    if os.getenv("DEMO") == "1":
        input_file = "2024\\01\\demo-input.txt"
    else:
        input_file = "2024\\01\\input.txt"
    return input_file


def get_sum_distances(first_list, second_list):
    total = sum([abs(first_list[i] - second_list[i]) for i in range(len(first_list))])
    return total


def get_similarity_score(first_list, second_list):
    similarity = 0
    for x in first_list:
        similarity += x * second_list.count(x)
    return similarity


if __name__ == "__main__":
    input_file = get_env()
    lines = get_file_lines(input_file)
    first_list = [int(line[0]) for line in lines]
    second_list = [int(line[1]) for line in lines]
    print(get_similarity_score(first_list, second_list))
    first_list.sort()
    second_list.sort()
    get_sum_distances(first_list, second_list)
    print(get_sum_distances(first_list, second_list))
