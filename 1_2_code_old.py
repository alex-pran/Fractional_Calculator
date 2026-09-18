from fractions import Fraction


def to_mixed_number(fraction):
    sign = "-" if fraction < 0 else ""
    fraction = abs(fraction)

    whole = fraction.numerator // fraction.denominator
    remainder = fraction.numerator % fraction.denominator

    if remainder == 0:
        return f"{sign}{whole}"
    elif whole == 0:
        return f"{sign}{remainder}/{fraction.denominator}"
    else:
        return f"{sign}{whole} {remainder}/{fraction.denominator}"


# def parse_fraction(user_input):
#     def tokenize_expression(expression):
#         tokens = []
#         current = ""
#
#         for char in expression:
#
#             if char in "+-*":
#                 if current.strip():
#                     tokens.append(current.strip())
#                     current = ""
#
#                 tokens.append(char)
#
#             elif char == "/":
#
#                 if "/" not in current and current.strip():
#                     current += char
#
#                 else:
#                     if current.strip():
#                         tokens.append(current.strip())
#                         current = ""
#
#                     tokens.append("/")
#
#             else:
#                 current += char
#
#         if current.strip():
#             tokens.append(current.strip())
#
#         return tokens
    def tokenize_expression(expression):
        tokens = []
        current = ""

        for i, char in enumerate(expression):

            if char in "+-*":
                if current.strip():
                    tokens.append(current.strip())
                    current = ""

                tokens.append(char)

            elif char == "/":

                # Если "/" находится внутри дроби,
                # оставляем его внутри текущего числа
                if "/" not in current and current.strip():
                    current += char

                else:
                    # Второй "/" — это операция деления
                    if current.strip():
                        tokens.append(current.strip())
                        current = ""

                    tokens.append("/")

            else:
                current += char

        if current.strip():
            tokens.append(current.strip())

        return tokens
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
        raise ValueError("Invalid fraction")

def evaluate_simple(tokens):
    result = parse_fraction(tokens[0])

    i = 1

    while i < len(tokens):

        operation = tokens[i]
        number = parse_fraction(tokens[i + 1])

        if operation == "+":
            result = result + number

        elif operation == "-":
            result = result - number

        elif operation == "*":
            result = result * number

        elif operation == "/":
            if number == 0:
                raise ZeroDivisionError

            result = result / number

        i += 2

    return result


def calculate(first_fraction, operation, second_fraction):

    if operation == "+":
        return first_fraction + second_fraction

    elif operation == "-":
        return first_fraction - second_fraction

    elif operation == "*":
        return first_fraction * second_fraction

    elif operation == "/":
        if second_fraction == 0:
            raise ZeroDivisionError

        return first_fraction / second_fraction

    else:
        raise ValueError("Unknown operation")

# while True:
#     first_input = input("Enter first fraction: ")
#     operation = input("Enter operation (+, -, *, /): ")
#     second_input = input("Enter second fraction: ")
#
#
#     try:
#         first_fraction = parse_fraction(first_input)
#         second_fraction = parse_fraction(second_input)
#
#         result = calculate(
#             first_fraction,
#             operation,
#             second_fraction
#         )
#
#         print(f"Result: {to_mixed_number(result)} ({float(result)})")
#
#
#     except ZeroDivisionError:
#         print("Error: Cannot divide by zero")
#
#     except ValueError:
#         print("Error: Invalid input")
#
#     again = input("Calculate again? (y/n): ")
#
#     if again.lower() != "y":
#         print("Goodbye!")
#         break

# def tokenize_expression(expression):
#     tokens = []
#     current = ""
#     for char in expression:
#
#         if char in "+-*" and not current.strip() and not tokens:
#             current += char
#             continue
#
#         if char in "+-*":
#             if current.strip():
#                 tokens.append(current.strip())
#                 current = ""
#
#             tokens.append(char)
#
#         elif char == "/":
#
#             if "/" not in current and current.strip():
#                 current += char
#
#             else:
#                 if current.strip():
#                     tokens.append(current.strip())
#                     current = ""
#
#                 tokens.append("/")
#
#         else:
#             current += char
#
#     if current.strip():
#         tokens.append(current.strip())
#
#     return tokens

def evaluate_simple(tokens):
    result = parse_fraction(tokens[0])

    i = 1

    while i < len(tokens):
        operation = tokens[i]
        number = parse_fraction(tokens[i + 1])

        if operation == "+":
            result = result + number

        elif operation == "-":
            result = result - number

        elif operation == "*":
            result = result * number

        elif operation == "/":
            if number == 0:
                raise ZeroDivisionError

            result = result / number

        i += 2

    return result

def press_button(expression, value):
    return expression + value

expression = ""
#expression = to_mixed_number(result)

while True:
    button = input("Press button: ")

    if button == "=":
        try:
            tokens = tokenize_expression(expression)
            result = evaluate_simple(tokens)

            print(f"Result: {to_mixed_number(result)} ({float(result)})")

            expression = str(result)

        except ZeroDivisionError:
            print("Error: Cannot divide by zero")
            expression = ""

        except (ValueError, TypeError, IndexError):
            print("Error: Invalid expression")
            expression = ""

        continue

    if button == "C":
        expression = ""
        print("Expression:", expression)
        continue

    if button == "<":
        expression = expression[:-1]
        print("Expression:", expression)
        continue

    expression = press_button(expression, button)

    print("Expression:", expression)

# buttons = ["1", "/", "2", "+", "3", "/", "4"]
#
# for button in buttons:
#     expression = press_button(expression, button)

# expression = press_button (expression, "1")
# expression = press_button(expression, "/")
# expression = press_button(expression, "2")
# expression = press_button(expression, "+")
# expression = press_button(expression, "3")
# expression = press_button(expression, "/")
# expression = press_button(expression, "4")

try:
    tokens = tokenize_expression(expression)
    result = evaluate_simple(tokens)
    print(f"Result: {to_mixed_number(result)} ({float(result)})")



except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except (ValueError, TypeError):
    print("Error: Invalid expression")

expression = str(result)
#continue


# def add_to_expressions(expressions, value):
#     return expressions + value
