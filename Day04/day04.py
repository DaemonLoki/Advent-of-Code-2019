# Challenges from https://adventofcode.com/2019/day/4

def read_input(file_name="Day04/day04.txt"):
    with open(file_name, "r") as f:
        return map(int, f.readline().split("-"))

def check_if_valid_password(num):
    two_adjacent_digits, prev_digit = False, None
    while num > 0:
        digit, num = num % 10, num // 10
        if prev_digit is None:
            prev_digit = digit
            continue
    
        # check for adjacent digits
        if digit == prev_digit:
            two_adjacent_digits = True

        # check for not decreasing
        if digit > prev_digit:
            return False

        # set digit to prev_digit
        prev_digit = digit
    
    return two_adjacent_digits

def run_input_tests():
    start, stop = read_input()
    assert start == 284639
    assert stop == 748759

def check_valid_password_tests():
    assert check_if_valid_password(111111)
    assert check_if_valid_password(223450) == False
    assert check_if_valid_password(123789) == False
 
def run_tests():
    run_input_tests()
    check_valid_password_tests()

run_tests()

start_index, end_index = read_input()
print(f"Start: {start_index}, End: {end_index}")

num_passwords = 0
for i in range(start_index, end_index + 1):
    num_passwords += 1 if check_if_valid_password(i) else 0

print(f"Number of valid password are {num_passwords}.")