from fractions import Fraction

from fractional import remainder


def mixed_fraction(fraction):
    whole =fraction.numerator // fraction.denominator
    remainder = fraction.numerator  % fraction.denominator

    if remainder == 0:
        return str(whole)

    if whole == 0:
        return f"{remainder}/{fraction.denominator}"

    return f"{whole} {remainder}/{fraction.denominator}"

def add_fraction(a, b):
    result = a + b
    result = mixed_fraction(result)

# Double Fraction
fraction1 = Fraction(1, 2)
fraction2 = Fraction(1, 3)

# sum
add_fraction(fraction1, fraction2)

# Total
print(result)





