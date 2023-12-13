import os.path
from sys import exit


def process_input(file_path: str) -> int:
    if not os.path.isfile(file_path):
        print("No input file!")
        exit(0)
    else:
        list_of_digits = []

        with open(file_path, 'r') as file:
            # Now ready line by line, file may be big
            for line in file:
                digits = process_line(line)
                if digits != "":
                    list_of_digits.append(digits)
        if len(list_of_digits) != 0:
            sum = 0
            for digit in list_of_digits:
                sum += int(digit)
            return sum


def process_line(line: str) -> str:
    first_digit = None
    last_digit = None

    for char in line:
        if char.isdigit():
            first_digit = char
            break

    for char in reversed(line):
        if char.isdigit():
            last_digit = char
            break

    if first_digit and last_digit is not None:
        return str(first_digit) + str(last_digit)
    elif first_digit is not None and last_digit is None:
        return first_digit
    elif last_digit is not None and first_digit is None:
        return last_digit

    return ""


if __name__ == '__main__':
    input_file_path = 'input.txt'
    sum = process_input(input_file_path)
    print(f"Sum is: {sum}")
