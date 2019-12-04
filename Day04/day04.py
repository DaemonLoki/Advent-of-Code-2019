# Challenges from https://adventofcode.com/2019/day/4

def read_input(file_name="Day04/day04.txt"):
    with open(file_name, "r") as f:
        return map(int, f.readline().split("-"))

def check_if_valid_password(num):
    two_adjacent_digits, prev_digit, currently_matching, match_count = False, None, False, 0
    while num > 0:
        digit, num = num % 10, num // 10
        if prev_digit is None:
            prev_digit = digit
            continue
    
        # check for adjacent digits
        if digit == prev_digit:
            if currently_matching == False:
                match_count = 2
            else:
                match_count += 1
            currently_matching = True
        else: 
            if match_count == 2:
                two_adjacent_digits = True
            match_count = 0
            currently_matching = False

        # check for not decreasing
        if digit > prev_digit:
            return False

        # set digit to prev_digit
        prev_digit = digit

    if match_count == 2:
        two_adjacent_digits = True
    
    return two_adjacent_digits

def run_input_tests():
    start, stop = read_input()
    assert start == 284639
    assert stop == 748759

def check_valid_password_tests():
    assert check_if_valid_password(111111) == False
    assert check_if_valid_password(223450) == False
    assert check_if_valid_password(123789) == False
    assert check_if_valid_password(112233)
    assert check_if_valid_password(123444) == False
    assert check_if_valid_password(111122)
    assert check_if_valid_password(112222)
 
def run_tests():
    run_input_tests()
    check_valid_password_tests()

    print("All tests passed.")

run_tests()

start_index, end_index = read_input()
print(f"Start: {start_index}, End: {end_index}")

num_passwords = 0
for i in range(start_index, end_index + 1):
    num_passwords += 1 if check_if_valid_password(i) else 0

print(f"Number of valid password are {num_passwords}.")