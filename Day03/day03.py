# Challenges from https://adventofcode.com/2019/day/3

def read_input(file_location):
    with open(file_location, "r") as f:
        first_wire = f.readline().split(",")
        second_wire = f.readline().split(",")
    return first_wire, second_wire

def update_min_distance(min_distance, x, y):
    dist = abs(x) + abs(y)
    if min_distance is None or dist < min_distance:
        print(f"Min distance changes from {min_distance} to {dist}.")
        min_distance = dist
    return min_distance

def extract_instruction(input):
    return input[0], int(input[1:])

def update_min_delay(min_delay, first_delay, second_delay):
    sum_delay = first_delay + second_delay
    if min_delay is None or sum_delay < min_delay:
        print(f"Min delay changes from {min_delay} to {sum_delay}.")
        min_delay = sum_delay
    return min_delay

def set_current_coordinates(dir, cur_x, cur_y, index):
    if dir == "R":
        return cur_x + index, cur_y
    elif dir == "L":
        return cur_x - index, cur_y
    elif dir == "U":
        return cur_x, cur_y + index
    elif dir == "D":
        return cur_x, cur_y - index

def layout_wire(wire, find_distance=False, prev_wire_positions=None):
    current_point, min_distance, min_delay, wire_positions, num_steps = (0, 0), None, None, {}, 0
    for i in wire:
        # get the current instruction
        direction, distance = extract_instruction(i)

        # check where we want to start iterating
        current_x, current_y = current_point[0], current_point[1]

        # check which axis we need to iterate on
        axis = current_x if direction in "LR" else current_y
        start_index, end_index = 1, distance + 1

        # iterate over the whole distance
        for j in range(start_index, end_index):
            num_steps += 1

            # set next coordinates depending on direction
            x_val, y_val = set_current_coordinates(direction, current_x, current_y, j)

            # update min_distance if necessary
            if find_distance and (x_val, y_val) in prev_wire_positions.keys():
                min_distance = update_min_distance(min_distance, x_val, y_val)
                min_delay = update_min_delay(min_delay, num_steps, prev_wire_positions[(x_val, y_val)])
            
            # update value in grid
            wire_positions[(x_val, y_val)] = num_steps
        
        # update the current point
        current_point = (x_val, y_val)

    return wire_positions, min_distance, min_delay

def perform_calculation(input_file="Day03/day03.txt", grid_size=20000):
    first_wire, second_wire = read_input(input_file)

    grid, grid_size = [], 20000
    for i in range(grid_size):
        grid.append(grid_size * ["."])

    starting_point = (grid_size // 2, grid_size // 2)
    grid[starting_point[0]][starting_point[1]] = "o"
    layed_out_grid, _, _ = layout_wire(first_wire)
    final_grid, min_dist, min_delay = layout_wire(second_wire, find_distance=True, prev_wire_positions=layed_out_grid)

    print(f"Min distance is: {min_dist}.")
    print(f"Min delay is: {min_delay}.")
    return min_dist

def test_read_input():
    test_wire_1, test_wire_2 = read_input("Day03/day03.txt")
    assert len(test_wire_1) == len(test_wire_2)
    assert len(test_wire_1) == 301

    test_wire_3, test_wire_4 = read_input("Day03/day03_test.txt")
    assert len(test_wire_3) == len(test_wire_4)
    assert len(test_wire_3) == 4

def test_distance_calc():
    assert update_min_distance(None, 4, 4) == 8
    assert update_min_distance(10, 4, 4) == 8
    assert update_min_distance(4, 4, 4) == 4
    assert update_min_distance(None, 89, 54) == 143

def test_extract_instructions():
    first_test = extract_instruction("R37")
    assert first_test[0] == "R"
    assert first_test[1] == 37

    second_test = extract_instruction("U12391")
    assert second_test[0] == "U"
    assert second_test[1] == 12391

    third_test = extract_instruction("L541")
    assert third_test[0] == "L"
    assert third_test[1] == 541

    fourth_test = extract_instruction("D1239048129")
    assert fourth_test[0] == "D"
    assert fourth_test[1] == 1239048129

def test_set_current_coordinates():
    x_1, y_1 = set_current_coordinates("R", 1, 1, 5)
    assert x_1 == 6
    assert y_1 == 1

    x_2, y_2 = set_current_coordinates("L", 15, 6, 10)
    assert x_2 == 5
    assert y_2 == 6

    x_3, y_3 = set_current_coordinates("U", 12, 8, 15)
    assert x_3 == 12
    assert y_3 == 23

    x_4, y_4 = set_current_coordinates("D", 15, 9, 3)
    assert x_4 == 15
    assert y_4 == 6

def run_tests():
    test_read_input()
    test_distance_calc()
    test_extract_instructions()
    test_set_current_coordinates()

    assert perform_calculation(input_file="Day03/day03_test.txt") == 6
    assert perform_calculation(input_file="Day03/day03_test_2.txt") == 159
    assert perform_calculation(input_file="Day03/day03_test_3.txt") == 135

    print("All tests passed.")
    print("-----------------")

run_tests()

perform_calculation()