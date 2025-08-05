import utils


if __name__ == "__main__":
    input_file = utils.get_input_file_by_env("04")
    grid = []
    for line in utils.get_clean_lines(input_file):
        grid.append(list(line[0]))
