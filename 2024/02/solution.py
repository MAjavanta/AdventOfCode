from dotenv import load_dotenv
import utils
import os


load_dotenv()


def get_env():
    if os.getenv("DEMO") == "1":
        input_file = "2024\\02\\demo-input.txt"
    else:
        input_file = "2024\\02\\input.txt"
    return input_file


def is_report_safe(line):
    differences = [int(line[i]) - int(line[i + 1]) for i in range(len(line) - 1)]
    safe_check = (
        all(i < 0 for i in differences) or all(i > 0 for i in differences),
        all(1 <= abs(i) <= 3 for i in differences),
    )
    return all(safe_check)


if __name__ == "__main__":
    report_safety_lst = []
    input_file = get_env()
    for line in utils.get_lines(input_file):
        report_safety_lst.append(is_report_safe(line))
    print(report_safety_lst.count(True))
