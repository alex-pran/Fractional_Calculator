
from fractions import Fraction
from math import remainder

user_input = input('Enter a fraction: ')
fraction = Fraction(user_input)
whole = fraction.numerator // fraction.denominator
remainder = fraction.numerator % fraction.denominator

if remainder == 0:
    print(f"Result: {whole}")

else:
    print(f"Result: {whole} {remainder}/{fraction.denominator}")