nttm = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

fttm = {
    1: "",
    2: "double ",
    3: "triple",
    4: "quadruple",
    5: "quintuple",
    6: "sextuple",
    7: "septuple",
    8: "octuple",
    9: "nontuple",
    10: "decuple"
}

n_test_cases = int(input())
for _ in range(1, n_test_cases + 1):
    number, phone_number_format = input().split(" ")
    number = list(number)
    phone_number_format = list(map(int, phone_number_format.split("-")))
    numbers = [ ]
    for format_index in phone_number_format:
        number_range = number[format_index:]
        for num in number_range:
            number.pop(0)
        numbers.append(number_range)
    print(numbers)
