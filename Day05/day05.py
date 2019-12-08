# Challenges from https://adventofcode.com/2019/day/5

def read_input():
    with open("Day05/day05.txt", "r") as f:
        puzzle = [int(x) for x in f.readline().split(",")]
    return puzzle

def get_values_from_instruction(raw_value):
    if raw_value < 100:
        return raw_value, [0, 0, 0]
    else:
        op_code, parameter_modes = raw_value % 100, raw_value // 100
        p_1, p_2, p_3 = parameter_modes % 10, parameter_modes // 10 % 10, parameter_modes // 100 % 10
        return op_code, [p_1, p_2, p_3]

    return raw_value

def solve_puzzle(puzzle):
    i = 0

    while i < len(puzzle):
        instruction, parameter_modes = get_values_from_instruction(puzzle[i])
        if instruction == 99:
            return puzzle[0]
        try:
            if instruction == 1:
                first_index, second_index, store_pos = puzzle[i+1], puzzle[i+2], puzzle[i+3]
                first_value = puzzle[first_index] if parameter_modes[0] == 0 else first_index
                second_value = puzzle[second_index] if parameter_modes[1] == 0 else second_index
                puzzle[store_pos] = first_value + second_value
                i += 4
            elif instruction == 2:
                first_index, second_index, store_pos = puzzle[i+1], puzzle[i+2], puzzle[i+3]
                first_value = puzzle[first_index] if parameter_modes[0] == 0 else first_index
                second_value = puzzle[second_index] if parameter_modes[1] == 0 else second_index
                puzzle[store_pos] = first_value * second_value
                i += 4
            elif instruction == 3:
                input_val = 5
                puzzle[puzzle[i+1]] = input_val
                i += 2
            elif instruction == 4:
                output_val = puzzle[i+1] if parameter_modes[0] == 1 else puzzle[puzzle[i+1]]
                print(output_val)
                i += 2
            elif instruction == 5:
                first_index, second_index = puzzle[i + 1], puzzle[i + 2]
                first_param = puzzle[first_index] if parameter_modes[0] == 0 else first_index
                second_param = puzzle[second_index] if parameter_modes[1] == 0 else second_index
                if first_param != 0:
                    i = second_param
                else:
                    i += 3
            elif instruction == 6:
                first_index, second_index = puzzle[i + 1], puzzle[i + 2]
                first_param = puzzle[first_index] if parameter_modes[0] == 0 else first_index
                second_param = puzzle[second_index] if parameter_modes[1] == 0 else second_index
                if first_param == 0:
                    i = second_param
                else:
                    i += 3
            elif instruction == 7:
                first_index, second_index, store_pos = puzzle[i + 1], puzzle[i + 2], puzzle[ i + 3]
                first_param = puzzle[first_index] if parameter_modes[0] == 0 else first_index
                second_param = puzzle[second_index] if parameter_modes[1] == 0 else second_index
                puzzle[store_pos] = 1 if first_param < second_param else 0
                i += 4
            elif instruction == 8:
                first_index, second_index, store_pos = puzzle[i + 1], puzzle[i + 2], puzzle[ i + 3]
                first_param = puzzle[first_index] if parameter_modes[0] == 0 else first_index
                second_param = puzzle[second_index] if parameter_modes[1] == 0 else second_index
                puzzle[store_pos] = 1 if first_param == second_param else 0
                i += 4
            else:
                return puzzle[0]
        except:
            print("Error occurred!")
            return puzzle[0]
            
def run_instruction_tests():
    op, params = get_values_from_instruction(3)
    assert op == 3 and len(params) == 3

    op, params = get_values_from_instruction(99)
    assert op == 99 and len(params) == 3

    op, params = get_values_from_instruction(102)
    assert op == 2
    assert len(params) == 3
    assert params[0] == 1 and params[1] == 0 and params[2] == 0

def run_tests():
    run_instruction_tests()

    print("All tests passed.")

run_tests()

puzzle = read_input()
solve_puzzle(puzzle)