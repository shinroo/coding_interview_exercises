import math


def add(a, b):
    while b:
        carry = a & b
        a, b = a ^ b, carry << 1
    return a


def multiply(x, y):
    running_sum = 0

    while x:
        if x & 1:
            running_sum = add(running_sum, y)
        x, y = x >> 1, y << 1
    return running_sum


def divide(x, y):
    result, power = 0, 32
    y_power = y << power
    while x >= y:
        while y_power > x:
            y_power >>= 1
            power -= 1

        result += 1 << power
        x -= y_power
    return result


def power(x, y):
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0 / x
    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1
    return result


def reverse_int(x):
    result = 0
    x_remaining = abs(x)

    while x_remaining:
        last_pos = x_remaining % 10
        result = result * 10 + last_pos
        x_remaining //= 10
    return -result if x < 0 else result


def reverse_int_from_string(x):
    x_str = str(abs(x))
    x_reversed = int(x_str[::-1])
    return -x_reversed if x < 0 else x_reversed


def is_palindrome_number(x):
    if x <= 0:
        return x == 0

    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10 ** (num_digits - 1)

    for i in range(num_digits // 2):
        if x // msd_mask != x % 10:
            return False
        x %= msd_mask
        x //= 10
        msd_mask //= 100
    return True


def is_intersecting(rec1, rec2):
    """
    rec1 and rec2 are lists of [x1, y1, x2, y2]
    i.e. only the coordinates without width and height
    where x1,x2 is the coordinate of bottom left corner
          y1, y2 coordinate of upper right corner

    """
    return not (
            rec1[2] <= rec2[0]
            or rec1[3] <= rec2[1]
            or rec1[0] >= rec2[2]
            or rec1[1] >= rec2[3]
    )
