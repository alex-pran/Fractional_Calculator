from fractions import Fraction


def to_mixed_number(fraction):
    sign = "-" if fraction < 0 else ""
    fraction = abs(fraction)

    whole = fraction.numerator // fraction.denominator
    remainder = fraction.numerator % fraction.denominator

    if remainder == 0:
        return f"{sign}{whole}"
    else:
        return f"{sign}{whole} {remainder}/{fraction.denominator}"


def parse_fraction(user_input):
    parts = user_input.split()

    if len(parts) == 1:
        return Fraction(parts[0])

    elif len(parts) == 2:
        whole = int(parts[0])
        fraction = Fraction(parts[1])

        if whole < 0:
            return whole - fraction
        else:
            return whole + fraction

    else:
        raise ValueError


first_input = input("Enter first fraction: ")
operation = input("Enter operation (+, -, *, /): ")
second_input = input("Enter second fraction: ")


try:
    first_fraction = parse_fraction(first_input)
    second_fraction = parse_fraction(second_input)

    if operation == "+":
        result = first_fraction + second_fraction

    elif operation == "-":
        result = first_fraction - second_fraction

    elif operation == "*":
        result = first_fraction * second_fraction

    elif operation == "/":
        if second_fraction == 0:
            print("Error: Cannot divide by zero")
            exit()
        else:
            result = first_fraction / second_fraction

    else:
        print("Error: Unknown operation")
        exit()

    print(f"Result: {to_mixed_number(result)}")


except:
    print("Error: Invalid fraction")