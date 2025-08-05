import utils
import re


def get_product(instruction):
    nums = instruction.removeprefix("mul(").removesuffix(")").split(",")
    return int(nums[0]) * int(nums[1])


def get_on_instructions(instruction_list):
    on_instructions = []
    read_instruction = True

    for instruction in instruction_list:
        if instruction == "do()":
            read_instruction = True
            continue
        elif instruction == "don't()":
            read_instruction = False
            continue
        elif read_instruction:
            on_instructions.append(instruction)
    return on_instructions


if __name__ == "__main__":
    good_instructions = []
    sum = 0
    input_file = utils.get_input_file_by_env("03")
    with open(input_file, "r") as f:
        for line in f.readlines():
            good_instructions += re.findall(
                r"mul\([0-9]+,[0-9]+\)|don't\(\)|do\(\)", line
            )
    on_instructions = get_on_instructions(good_instructions)
    for instruction in on_instructions:
        sum += get_product(instruction)
    print(sum)
