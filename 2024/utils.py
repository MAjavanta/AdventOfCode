from dotenv import load_dotenv
import os


load_dotenv()


def get_clean_lines(input_file):
    with open(input_file, "r") as f:
        for line in f:
            lst = line.strip().split()
            yield lst


def get_input_file_by_env(day):
    if os.getenv("DEMO") == "1":
        input_file = f"2024\\{day}\\demo-input.txt"
    else:
        input_file = f"2024\\{day}\\input.txt"
    return input_file
