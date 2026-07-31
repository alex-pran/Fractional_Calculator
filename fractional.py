
from fractions import Fraction
from math import remainder
numerator1 = int(input('Enter first numerator: '))
denominator1 = int(input('Enter first denominator: '))

numerator2 = int(input('Enter second numerator: '))
denumerator2 = int(input('Enter second denumerator: '))

a = Fraction(numerator1, denominator1)
b = Fraction(numerator2, denumerator2)

result = a + b

whole = result.numerator // result.denominator
remainder = result.numerator % result.denominator

print(f'{whole} {remainder}/{result.denominator}')