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

def format_result(result):
    return f"{to_mixed_number(result)} ({float(result)})"

ALLOWED_BUTTONS = "0123456789+-*/=C< "

def handle_button(expression, button):
    if button not in ALLOWED_BUTTONS:
        return expression, "Error: Invalid button"


    if button == "C":
        return "", ""

    if button == "<":
        return expression[:-1], ""

    if button == "=":
        try:
            tokens = tokenize_expression(expression)
            result = evaluate_simple(tokens)

            return str(result), f"Result: {format_result(result)}"

        except ZeroDivisionError:
            return "", "Error: Cannot divide by zero"

        except (ValueError, TypeError, IndexError):
            return "", "Error: Invalid expression"

    return expression + button, ""

# def press_button(expression, value):
#     return expression + value
class Calculator:
    def __init__(self):
        self.expression = ""

    def press(self, button):
        self.expression, message = handle_button(
            self.expression,
            button
        )

        return self.expression, message

def run_calculator():
    calculator = Calculator()

    while True:
        button = input("Press button: ")

        expression, message = calculator.press(button)

        if message:
            print(message)
        else:
            print("Expression:", expression)


run_calculator()
