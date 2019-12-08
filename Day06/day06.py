# Challenges from https://adventofcode.com/2019/day/6

def read_input(filename="Day06/day06.txt"):
    with open(filename, "r") as f:
        orbits = [x.strip().split(")") for x in f]
    return orbits

def get_orbit_map(orbits):
    orbit_map = {}
    for orbit in orbits:
        orbit_map[orbit[1]] = orbit[0]
    return orbit_map

def get_orbit_counts(orbit_map):
    number_of_orbits, orbit_counts = 0, {}
    for planet in orbit_map.keys():
        current_orbits = 0
        cur_planet = planet
        while True:
            try:
                cur_planet = orbit_map[cur_planet]
                current_orbits += 1
                if cur_planet in orbit_counts.keys():
                    current_orbits += orbit_counts[cur_planet]
                    break 
            except KeyError:
                break
        orbit_counts[planet] = current_orbits
    return orbit_counts

def find_number_of_orbits(test=False):
    orbits = read_input(filename="Day06/day06_test.txt") if test else read_input()
    orbit_map = get_orbit_map(orbits)
    
    orbit_counts = get_orbit_counts(orbit_map)
    return sum(orbit_counts.values()), orbit_map

def find_min_number_of_orbital_transfers(orbit_map):
    you_arr = []
    cur_planet = orbit_map["YOU"]
    while True:
        you_arr.append(cur_planet)
        try:
            cur_planet = orbit_map[cur_planet]
        except KeyError:
            break

    cur_planet, san_count = orbit_map["SAN"], 0
    while True:
        if cur_planet in you_arr:
            return san_count + you_arr.index(cur_planet)
        else:
            try:
                cur_planet = orbit_map[cur_planet]
                san_count += 1  
            except KeyError:
                print("Error occurred!")
                break


def run_input_tests():
    orbits_1 = read_input()
    assert len(orbits_1) == 2113
    for orbit in orbits_1:
        assert len(orbit) == 2

    orbits_2 = read_input(filename="Day06/day06_test.txt")
    assert len(orbits_2) == 13
    for orbit in orbits_2:
        assert len(orbit) == 2

def run_orbit_map_tests():
    i1, i2 = read_input(), read_input(filename="Day06/day06_test.txt")
    orbit_map_1 = get_orbit_map(i1)
    assert len(orbit_map_1) == len(i1)

    orbit_map_2 = get_orbit_map(i2)
    assert len(orbit_map_2) == len(i2)

def run_orbit_counts_test():
    orbit_map = get_orbit_map(read_input(filename="Day06/day06_test.txt"))
    orbit_counts = get_orbit_counts(orbit_map)
    assert orbit_counts["B"] == 1
    assert orbit_counts["D"] == 3
    assert orbit_counts["L"] == 7
    
def run_puzzle_solve_tests():
    num_of_orbits = find_number_of_orbits(test=True)
    assert num_of_orbits == 42

def run_min_number_tests():
    _, orbit_map = find_number_of_orbits(test=True)
    min_number_of_orbits = find_min_number_of_orbital_transfers(orbit_map)
    assert min_number_of_orbits == 4

def run_tests():
    run_input_tests()
    run_orbit_map_tests()
    run_orbit_counts_test()
    #run_puzzle_solve_tests()
    run_min_number_tests()

    print("All tests passed")

run_tests()

number_of_orbits, orbit_map = find_number_of_orbits()
print(f"The number of total orbits is {number_of_orbits}.")

min_number_of_orbits = find_min_number_of_orbital_transfers(orbit_map)
print(f"The minimum number of orbits I have to take is {min_number_of_orbits}.")