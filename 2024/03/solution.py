import utils
import re


def get_product(instruction):
    nums = instruction.removeprefix("mul(").removesuffix(")").split(",")
    return int(nums[0]) * int(nums[1])


if __name__ == "__main__":
    good_instructions = []
    sum = 0
    input_file = utils.get_input_file_by_env("03")
    with open(input_file, "r") as f:
        for line in f.readlines():
            good_instructions += re.findall(r"mul\([0-9]+,[0-9]+\)", line)
    for instruction in good_instructions:
        sum += get_product(instruction)
    print(sum)
