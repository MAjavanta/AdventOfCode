def get_lines(input_file):
    with open(input_file, "r") as f:
        for line in f:
            lst = line.strip().split()
            yield lst
