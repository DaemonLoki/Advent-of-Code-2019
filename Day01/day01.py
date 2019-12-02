# Challenges from https://adventofcode.com/2019/day/1
def read_input():
    with open("day01.txt", "r") as f:
        module_masses = [x.strip() for x in f if x is not None]
    return module_masses

module_masses = read_input()
print(module_masses)