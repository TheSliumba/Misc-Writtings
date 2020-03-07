"""
3A5C
​
"AAA" "CCCCC"
ACCCCCACCCCCACCCCC
​
"""

def transformacija(tekstas):
    """
    >>> transformacija("3A5C")
    'ACCCCCACCCCCACCCCC'
​
    :param tekstas:
    :return:
    """
    digit_info = ''
    letters = []

    for i in tekstas:
        if i.isdigit():
            digit_info += i
        else:
            letters.append(i)
            digit_info += ' '

    resulting_letters = ''

    digits = [int(digit) for digit in digit_info.split()]
    k = 1

    for i in range(digits.pop(0)):
        resulting_letters += letters[0] + digits[i]*letters[k]
        k


    return resulting_letters


if __name__ == '__main__':
    import doctest
    #doctest.testmod(verbose=True)
    yup = transformacija("4A5B")
    print(yup)