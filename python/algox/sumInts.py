def sum(x: int, y: int) -> int:
    """
    Given two integers a and b, return the sum of the two integers without using the operators + and -.
    Analysis:
    use bit operations
    """
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1

    return x


if __name__ == "__main__":
    x = 3
    y = 12
    print(sum(x, y))


