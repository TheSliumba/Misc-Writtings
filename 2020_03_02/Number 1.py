"""
Trying for the n-th time to write a working roman numeral converter without outside help
"""


def convert_to_roman(number: int):
    """
    Put in an integer and gaze upon the wonders of roman numerals

    :param number: Integer
    :return: String roman numeral representation of said integer
    """
    letters = ["M", "CM", "D", "CD", "C", "CL", "L", "XL", "X", "IX", "V", "IV", "I"]
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = ''
    i = 0
    while number > 0:
        for _ in range(number // values[i]):
            result += letters[i]
            number -= values[i]
        i += 1
    return result


print(convert_to_roman(1936))
