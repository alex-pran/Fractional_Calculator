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
        raise ValueError("Invalid fraction")


def tokenize_expression(expression):
    tokens = []
    current = ""

    i = 0

    while i < len(expression):
        char = expression[i]

        # Операторы + - *
        if char in "+-*":

            if char == "-" and not current and (
                not tokens or tokens[-1] in "+-*/"
            ):
                current = "-"

            else:
                if current:
                    tokens.append(current)
                    current = ""

                tokens.append(char)

        # /
        elif char == "/":

            # Если следующий символ "-" —
            # этот / является оператором деления
            if i + 1 < len(expression) and expression[i + 1] == "-":
                if current:
                    tokens.append(current)
                    current = ""

                tokens.append("/")

            # Иначе / является частью дроби
            elif current and "/" not in current:
                current += "/"

            else:
                if current:
                    tokens.append(current)
                    current = ""

                tokens.append("/")

        else:
            current += char

        i += 1

    if current:
        tokens.append(current)

    return tokens


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


while True:
    button = input("Press button: ")

    if button == "=":

        try:
            tokens = tokenize_expression(expression)
            #print("TOKENS:", tokens)
            result = evaluate_simple(tokens)

            print(
                f"Result: {to_mixed_number(result)} "
                f"({float(result)})"
            )

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