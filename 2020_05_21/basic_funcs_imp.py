"""
This here file is me trying to write basic built-ins that python has already
It is just practice to stay on game if you will, always use builtins unless a big
need arises. Such life is.
"""


def minimal(numbers: list):
    """

    :param numbers: input a list of integers, don't use lists with strings or anything else
    :return: minimal value in said list
    """
    val = None
    for i in numbers:
        if val is None:
            val = i
        else:
            if i < val:
                val = i
    return val


def maximum(numbers: list):
    """

    :param numbers: input a list of integers, don't use lists with strings or nothing else
    :return: maximum value in said list
    """
    val = None
    for i in numbers:
        if val is None:
            val = i
        else:
            if i > val:
                val = i
    return val


def summing(numbers: list):
    """

    :param numbers: list of integers
    :return: sum value of list
    """
    val = 0
    for i in numbers:
        val += i
    return val


def average(numbers: list):
    """

    :param numbers: list of integers
    :return: average value of list
    """
    return summing(numbers) / len(numbers)


if __name__ == '__main__':
    sar = [4, 6, 3, 4, 2, 8, 7, 6, 4, 123, 567, 234]
    value_min = minimal(sar)
    value_max = maximum(sar)
    value_sum = summing(sar)
    value_avg = average(sar)
    print(f"Minimal value: {value_min}, Maximum value: {value_max}, "
          f"Total sum value: {value_sum}, Average value: {value_avg:02}")
