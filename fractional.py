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

    def clear(self):
        self.expression = ""
        self.result_shown = False

    def backspace(self):
        self.expression = self.expression[:-1]
        self.result_shown = False

    def press_equals(self):
        try:
            result = self.calculate()

            self.expression = str(result)
            self.result_shown = True

            return self.expression, f"Result: {format_result(result)}"

        except ZeroDivisionError:
            self.clear()
            return self.expression, "Error: Cannot divide by zero"

        except (ValueError, TypeError, IndexError):
            self.clear()
            return self.expression, "Error: Invalid expression"

    def press(self, button):

        if button not in self.allowed_buttons:
            return self.expression, "Error: Invalid button"

        if button == "C":
            self.clear()
            return self.expression, ""

        if button == "<":
            self.backspace()
            return self.expression, ""

        if button == "=":
            return self.press_equals()

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


# TESTS

def run_tests():
    all_passed = True

    def run_test(expression, expected):
        calculator = Calculator()
        calculator.expression = expression

        expression_result, message = calculator.press_equals()

        print("Test:", expression)
        print("Result:", message)

        if message == expected:
            print("PASSED")
        else:
            print("FAILED")
            print("Expected:", expected)
            nonlocal all_passed
            all_passed = False

        print()


    tests = [
        ("1/2+1/4", "Result: 3/4 (0.75)"),
        ("1 1/2+1 1/4", "Result: 2 3/4 (2.75)"),
        ("-1/2+3/4", "Result: 1/4 (0.25)"),
        ("3/4*2/3", "Result: 1/2 (0.5)"),
        ("3/4/2/3", "Result: 1 1/8 (1.125)"),
        ("-1 1/2+2", "Result: 1/2 (0.5)"),
        ("1+-1 1/2", "Result: -1/2 (-0.5)"),
        ("1*-1 1/2", "Result: -1 1/2 (-1.5)"),
        ("1+2*3", "Result: 9 (9.0)"),
    ]


    for expression, expected in tests:
        run_test(expression, expected)


    # Error tests

    calculator = Calculator()

    calculator.expression = "1/0"
    expression_result, message = calculator.press_equals()

    if message == "Error: Cannot divide by zero":
        print("Divide by zero PASSED")
    else:
        print("Divide by zero FAILED")
        all_passed = False


    calculator.expression = "1+"
    expression_result, message = calculator.press_equals()

    if message == "Error: Invalid expression":
        print("Invalid expression PASSED")
    else:
        print("Invalid expression FAILED")
        all_passed = False


    # Button tests

    calculator.clear()
    calculator.expression = "123"
    calculator.backspace()

    if calculator.expression == "12":
        print("Backspace PASSED")
    else:
        print("Backspace FAILED")
        all_passed = False


    calculator.expression = "123"
    calculator.clear()

    if calculator.expression == "":
        print("Clear PASSED")
    else:
        print("Clear FAILED")
        all_passed = False


    # Result state tests

    calculator.clear()
    calculator.expression = "1+2"

    calculator.press_equals()
    calculator.press("5")

    if calculator.expression == "5":
        print("New expression after result PASSED")
    else:
        print("New expression after result FAILED")


    calculator.clear()
    calculator.expression = "1+2"

    calculator.press_equals()
    calculator.press("+")
    calculator.press("4")

    expression_result, message = calculator.press_equals()

    if message == "Result: 7 (7.0)":
        print("Continue after result PASSED")
    else:
        print("Continue after result FAILED")


    # Repeated equals test

    calculator.clear()
    calculator.expression = "1+2"

    expression_result, message1 = calculator.press_equals()
    expression_result, message2 = calculator.press_equals()

    if message1 == "Result: 3 (3.0)" and message2 == "Result: 3 (3.0)":
        print("Repeated equals PASSED")
    else:
        print("Repeated equals FAILED")

        print()

    if all_passed:
        print("ALL TESTS PASSED")
    else:
        print("SOME TESTS FAILED")


if __name__ == "__main__":
    #run_tests()
    run_calculator()