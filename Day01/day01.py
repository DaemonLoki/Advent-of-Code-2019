# Challenges from https://adventofcode.com/2019/day/1
def read_input():
    with open("Day01/day01.txt", "r") as f:
        module_masses = [int(x.strip()) for x in f if x is not None]
    return module_masses

def calculate_single_requirement(mass):
    return mass // 3 - 2

def compute_additional_fuel(module):
    fuel_required = calculate_single_requirement(module)
    if fuel_required <= 0:
        return 0
    else:
        return fuel_required + compute_additional_fuel(fuel_required) 

def compute_fuel_requirements(module_masses):
    module_requirements = [calculate_single_requirement(x) for x in module_masses]
    for index, module in enumerate(module_requirements):
        module_requirements[index] += compute_additional_fuel(module)
    return sum(module_requirements)

module_masses = read_input()
fuel_requirements = compute_fuel_requirements(module_masses)
print(f"The fuel requirements are: {fuel_requirements}.")