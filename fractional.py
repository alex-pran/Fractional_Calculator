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

            if char in "+-" and not current and (
                not tokens or tokens[-1] in "+-*/"
            ):
                current = char

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


# ALLOWED_BUTTONS = "0123456789+-*/=C< "




class Calculator:
    def __init__(self):
        self.expression = ""
        self.allowed_buttons = "0123456789+-*/=C< "
        self.result_shown = False

    def calculate(self):
        if not self.expression:
            raise ValueError("Empty expression")

        tokens = tokenize_expression(self.expression)
        return evaluate_simple(tokens)

    def press(self, button):
        if button not in self.allowed_buttons:
            return self.expression, "Error: Invalid button"

        if button == "C":
            self.expression = ""
            self.result_shown = False
            return self.expression, ""

        if button == "<":
            self.expression = self.expression[:-1]
            self.result_shown = False
            return self.expression, ""

        if button == "=":
            try:
                result = self.calculate()

                self.expression = str(result)
                self.result_shown = True # added

                return self.expression, f"Result: {format_result(result)}"

            except ZeroDivisionError:
                self.expression = ""
                return self.expression, "Error: Cannot divide by zero"

            except (ValueError, TypeError, IndexError):
                self.expression = ""
                return self.expression, "Error: Invalid expression"

        if self.result_shown:
            if button not in "+-*/":
                self.expression = ""

            self.result_shown = False

        self.expression += button
        return self.expression, ""


def run_calculator():
    calculator = Calculator()

    while True:
        button = input("Press button: ")

        expression, message = calculator.press(button)

        if message:
            print(message)
        else:
            print("Expression:", expression)

calculator = Calculator()
calculator.expression = "1/2+1/2"
print(calculator.calculate())

run_calculator()