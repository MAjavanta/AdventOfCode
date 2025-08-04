from dotenv import load_dotenv
import utils


def is_report_safe(line):
    differences = [int(line[i]) - int(line[i + 1]) for i in range(len(line) - 1)]
    safe_check = (
        all(i < 0 for i in differences) or all(i > 0 for i in differences),
        all(1 <= abs(i) <= 3 for i in differences),
    )
    return all(safe_check)


if __name__ == "__main__":
    report_safety_lst = []
    input_file = utils.get_input_file_by_env("02")
    for line in utils.get_clean_lines(input_file):
        if is_report_safe(line):
            report_safety_lst.append(True)
        else:
            for i in range(len(line)):
                reduced_line = line[:i] + line[i + 1 :]
                if is_report_safe(reduced_line):
                    report_safety_lst.append(True)
                    break
    print(report_safety_lst.count(True))
