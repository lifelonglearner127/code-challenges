def solve(n):
    if n < 1000:
        return str(n)
    else:
        divisor = 1000
        quotient = n // divisor
        remainder = n % divisor
        return solve(quotient) + ',' + str(remainder)


def main():
    numbers = [
        (1, '1'),
        (12, '12'),
        (123, '123'),
        (1234, '1,234'),
        (12345, '12,345'),
        (1234567, '1,234,567'),
        (12345678, '12,345,678'),
        (123456789, '123,456,789'),
    ]
    for number, string in numbers:
        assert solve(number) == string


if __name__ == '__main__':
    main()
