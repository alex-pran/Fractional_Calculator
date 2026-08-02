from fractions import Fraction
from math import remainder
from unittest import result

def to_mixed_number(fraction):
    whole = fraction.numerator // fraction.denominator
    reminder = fraction.numerator % fraction.denominator

    if reminder == 0:
        return str(whole)
    else:
        return f"{whole} / {reminder}/{fraction.denominator}"

first_input = input("Enter first fraction: ")
operation = input("Enter operation (+, -, *, /): ")
second_input = input("Enter second fraction: ")
try:
    first_fraction = Fraction(first_input)
    second_fraction = Fraction(second_input)

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
    print("Error:Invalid fraction")