"""implements add and subtract functions taking “unlimited” number of params"""
"""more feature added: multiplication and division"""


def add(*args):

    return sum(args)


def sub(*args):
    """
    Return the first arg minus all the following args.
    """
    diff = args[0]
    for i in args[1:]:
        diff -= i
    return diff


def mul(a: int | float, b: int | float):

    return a * b

# hello
# Goodbye


def div(a: int | float, b: int | float):

    return a / b
