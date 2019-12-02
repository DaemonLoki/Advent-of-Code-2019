# Challenges from https://adventofcode.com/2019/day/1
def read_input():
    with open("Day01/day01.txt", "r") as f:
        module_masses = [int(x.strip()) for x in f if x is not None]
    return module_masses

def compute_fuel_requirements(module_masses):
    return sum([x // 3 - 2 for x in module_masses])

module_masses = read_input()
fuel_requirements = compute_fuel_requirements(module_masses)
print(f"The fuel requirements are: '{fuel_requirements}'")