# Challenges from https://adventofcode.com/2019/day/2

def read_input():
    with open("Day02/day02.txt", "r") as f:
        puzzle = [int(x) for x in f.readline().split(",")]
    return puzzle

def solve_puzzle(puzzle):
    assert len(puzzle) > 3
    puzzle[1], puzzle[2] = 12, 2

    for i in range(0, len(puzzle), 4):
        if puzzle[i] == 99:
            return puzzle[0]
        try:
            first_index, second_index, store_pos = puzzle[i+1], puzzle[i+2], puzzle[i+3]
            if puzzle[i] == 1:
                puzzle[store_pos] = puzzle[first_index] + puzzle[second_index]
            elif puzzle[i] == 2:
                puzzle[store_pos] = puzzle[first_index] * puzzle[second_index]
            else:
                return puzzle[0]
        except:
            return puzzle[0]

def find_input_pair():
    for noun in range(0, 100):
        for verb in range(0, 100):
            puzzle = read_input()
            puzzle[1], puzzle[2] = noun, verb

            for i in range(0, len(puzzle), 4):
                instruction = puzzle[i]
                if instruction == 99:
                    if puzzle[0] == 19690720:
                        return 100 * noun + verb
                    break
                try:
                    first_index, second_index, store_pos = puzzle[i+1], puzzle[i+2], puzzle[i+3]
                    if instruction == 1:
                        puzzle[store_pos] = puzzle[first_index] + puzzle[second_index]
                    else:
                        puzzle[store_pos] = puzzle[first_index] * puzzle[second_index]
                except:
                    print(f"Reached KeyError for {noun}, {verb}")
                    break

puzzle = read_input()
final_val = solve_puzzle(puzzle)
print(f"Final value is {final_val}")

noun_verb_comb = find_input_pair()
print(f"The result of the combination is {noun_verb_comb}")