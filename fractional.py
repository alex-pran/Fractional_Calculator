from fractions import Fraction
from math import remainder
from unittest import result

first_input = input("Enter first fraction: ")
operation = input("Enter operation (+, -, *, /): ")
second_input = input("Enter second fraction: ")

first_fraction = Fraction(first_input)
second_fraction = Fraction(second_input)

if operation == "+":
    result = first_fraction + second_fraction

elif operation == "-":
    result = first_fraction - second_fraction

elif operation == "*":
    result = first_fraction * second_fraction

elif operation == "/":
    result = first_fraction / second_fraction

else:
    print("Unknown operation")
    exit()

whole = result.numerator // result.denominator
remainder = result.numerator % result.denominator

if remainder == 0:
    print(f"Result: {whole}")

else:
    print(f"Result: {whole} / {remainder}/{result.denominator}")