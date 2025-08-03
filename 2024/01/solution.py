import utils


def get_sum_distances(first_list, second_list):
    total = sum([abs(first_list[i] - second_list[i]) for i in range(len(first_list))])
    return total


def get_similarity_score(first_list, second_list):
    similarity = 0
    for x in first_list:
        similarity += x * second_list.count(x)
    return similarity


if __name__ == "__main__":
    input_file = utils.get_input_file_by_env("01")
    first_list = [int(line[0]) for line in utils.get_lines(input_file)]
    second_list = [int(line[1]) for line in utils.get_lines(input_file)]
    print(get_similarity_score(first_list, second_list))
    first_list.sort()
    second_list.sort()
    get_sum_distances(first_list, second_list)
    print(get_sum_distances(first_list, second_list))
