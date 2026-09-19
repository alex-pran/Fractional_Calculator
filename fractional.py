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

        elif char == "/":

            if i + 1 < len(expression) and expression[i + 1] == "-":
                if current:
                    tokens.append(current)
                    current = ""

                tokens.append("/")

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

    def get_result(self):
        return self.calculate()

    def is_result_shown(self):
        return self.result_shown

    def get_display(self):
        if self.result_shown:
            return format_result(self.get_result())

        return self.expression

    def get_state(self):
        return {
            "expression": self.get_expression(),
            "display": self.get_display(),
            "result_shown": self.is_result_shown()
        }

    def clear(self):
        self.expression = ""
        self.result_shown = False

    def get_expression(self):
        return self.expression

    def backspace(self):
        self.expression = self.expression[:-1]
        self.result_shown = False

    def press_equals(self):
        try:
            result = self.calculate()

            self.expression = str(result)
            self.result_shown = True

            return f"Result: {self.get_display()}"

        except ZeroDivisionError:
            self.clear()
            return "Error: Cannot divide by zero"

        except (ValueError, TypeError, IndexError):
            self.clear()
            return "Error: Invalid expression"

    def press_and_get_state(self, button):
        _, message = self.press(button)

        return {
            "expression": self.get_expression(),
            "display": self.get_display(),
            "result_shown": self.is_result_shown(),
            "message": message
        }

    def press(self, button):

        if button not in self.allowed_buttons:
            return self.expression, "Error: Invalid button"

        if button == "C":
            self.clear()
            return self.get_display(), ""

        if button == "<":
            self.backspace()
            return self.get_display(), ""

        if button == "=":
            message = self.press_equals()
            return self.get_display(), message

        if self.result_shown:
            if button not in "+-*/":
                self.expression = ""

            self.result_shown = False

        self.expression += button

        return self.get_display(), ""


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
        nonlocal all_passed

        calculator = Calculator()
        calculator.expression = expression

        message = calculator.press_equals()

        print("Test:", expression)
        print("Result:", message)

        if message == expected:
            print("\033[92mPASSED\033[0m")
        else:
            print("\033[91mFAILED\033[0m")
            print("Expected:", expected)
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
    message = calculator.press_equals()

    if message == "Error: Cannot divide by zero":
        print("Divide by zero \033[92mPASSED\033[0m")
    else:
        print("Divide by zero \033[91mFAILED\033[0m")
        all_passed = False

    calculator.expression = "1+"
    message = calculator.press_equals()

    if message == "Error: Invalid expression":
        print("Invalid expression \033[92mPASSED\033[0m")
    else:
        print("Invalid expression \033[91mFAILED\033[0m")
        all_passed = False

    # Button tests

    calculator.clear()
    calculator.expression = "123"
    calculator.backspace()

    if calculator.expression == "12":
        print("Backspace \033[92mPASSED\033[0m")
    else:
        print("Backspace \033[91mFAILED\033[0m")
        all_passed = False

    calculator.expression = "123"
    calculator.clear()

    if calculator.expression == "":
        print("Clear \033[92mPASSED\033[0m")
    else:
        print("Clear \033[91mFAILED\033[0m")
        all_passed = False

    # Get expression test

    calculator.clear()
    calculator.press("1")
    calculator.press("/")
    calculator.press("2")

    if calculator.get_expression() == "1/2":
        print("Get expression \033[92mPASSED\033[0m")
    else:
        print("Get expression \033[91mFAILED\033[0m")
        all_passed = False

    # Get result test

    calculator.clear()
    calculator.expression = "1/2+1/4"

    if calculator.get_result() == Fraction(3, 4):
        print("Get result \033[92mPASSED\033[0m")
    else:
        print("Get result \033[91mFAILED\033[0m")
        all_passed = False

    # Result state tests

    calculator.clear()
    calculator.expression = "1+2"

    calculator.press_equals()
    calculator.press("5")

    if calculator.expression == "5":
        print("New expression after result \033[92mPASSED\033[0m")
    else:
        print("New expression after result \033[91mFAILED\033[0m")
        all_passed = False

    calculator.clear()
    calculator.expression = "1+2"

    calculator.press_equals()
    calculator.press("+")
    calculator.press("4")

    message = calculator.press_equals()

    if message == "Result: 7 (7.0)":
        print("Continue after result \033[92mPASSED\033[0m")
    else:
        print("Continue after result \033[91mFAILED\033[0m")
        all_passed = False

    # Repeated equals test

    calculator.clear()
    calculator.expression = "1+2"

    message1 = calculator.press_equals()
    message2 = calculator.press_equals()

    if message1 == "Result: 3 (3.0)" and message2 == "Result: 3 (3.0)":
        print("Repeated equals \033[92mPASSED\033[0m")
    else:
        print("Repeated equals \033[91mFAILED\033[0m")
        all_passed = False

    # Result shown test

    calculator.clear()
    calculator.expression = "1+2"

    if not calculator.is_result_shown():
        print("Before equals \033[92mPASSED\033[0m")
    else:
        print("Before equals \033[91mFAILED\033[0m")
        all_passed = False

    calculator.press_equals()

    if calculator.is_result_shown():
        print("After equals \033[92mPASSED\033[0m")
    else:
        print("After equals \033[91mFAILED\033[0m")
        all_passed = False

    # Get display test

    calculator.clear()
    calculator.press("1")
    calculator.press("/")
    calculator.press("2")

    if calculator.get_display() == "1/2":
        print("Display expression \033[92mPASSED\033[0m")
    else:
        print("Display expression \033[91mFAILED\033[0m")
        all_passed = False

    calculator.press("+")
    calculator.press("1")
    calculator.press("/")
    calculator.press("4")
    calculator.press_equals()

    if calculator.get_display() == "3/4 (0.75)":
        print("Display result \033[92mPASSED\033[0m")
    else:
        print("Display result \033[91mFAILED\033[0m")
        all_passed = False

    # Get state test

    calculator.clear()
    calculator.press("1")
    calculator.press("/")
    calculator.press("2")

    state = calculator.get_state()

    if (
        state["expression"] == "1/2"
        and state["display"] == "1/2"
        and state["result_shown"] is False
    ):
        print("Get state before result \033[92mPASSED\033[0m")
    else:
        print("Get state before result \033[91mFAILED\033[0m")
        all_passed = False

    calculator.press("+")
    calculator.press("1")
    calculator.press("/")
    calculator.press("2")
    calculator.press_equals()

    state = calculator.get_state()

    if (
        state["expression"] == "1"
        and state["display"] == "1 (1.0)"
        and state["result_shown"] is True
    ):
        print("Get state after result \033[92mPASSED\033[0m")
    else:
        print("Get state after result \033[91mFAILED\033[0m")
        all_passed = False

    # Press and get state test

    calculator.clear()

    state = calculator.press_and_get_state("1")

    if (
        state["expression"] == "1"
        and state["display"] == "1"
        and state["result_shown"] is False
        and state["message"] == ""
    ):
        print("Press and get state \033[92mPASSED\033[0m")
    else:
        print("Press and get state \033[91mFAILED\033[0m")
        all_passed = False

    # Press and get state equals

    calculator.clear()
    calculator.press("1")
    calculator.press("+")
    calculator.press("2")

    state = calculator.press_and_get_state("=")

    if (
        state["expression"] == "3"
        and state["display"] == "3 (3.0)"
        and state["result_shown"] is True
        and state["message"] == "Result: 3 (3.0)"
    ):
        print("Press and get state equals \033[92mPASSED\033[0m")
    else:
        print("Press and get state equals \033[91mFAILED\033[0m")
        all_passed = False

    # Press invalid button test

    calculator.clear()

    state = calculator.press_and_get_state("X")

    if (
        state["expression"] == ""
        and state["display"] == ""
        and state["result_shown"] is False
        and state["message"] == "Error: Invalid button"
    ):
        print("Press invalid button \033[92mPASSED\033[0m")
    else:
        print("Press invalid button \033[91mFAILED\033[0m")
        all_passed = False

    # Press digit after result test

    calculator.clear()
    calculator.press("1")
    calculator.press("+")
    calculator.press("2")
    calculator.press_equals()

    state = calculator.press_and_get_state("5")

    if (
        state["expression"] == "5"
        and state["display"] == "5"
        and state["result_shown"] is False
        and state["message"] == ""
    ):
        print("Press digit after result \033[92mPASSED\033[0m")
    else:
        print("Press digit after result \033[91mFAILED\033[0m")
        all_passed = False

    # Press and get state C

    calculator.clear()
    calculator.press("1")
    calculator.press("+")
    calculator.press("2")

    state = calculator.press_and_get_state("C")

    if (
        state["expression"] == ""
        and state["display"] == ""
        and state["result_shown"] is False
        and state["message"] == ""
    ):
        print("Press and get state C \033[92mPASSED\033[0m")
    else:
        print("Press and get state C \033[91mFAILED\033[0m")
        all_passed = False

    # Press and get state backspace

    calculator.clear()
    calculator.press("1")
    calculator.press("/")
    calculator.press("2")

    state = calculator.press_and_get_state("<")

    if (
        state["expression"] == "1/"
        and state["display"] == "1/"
        and state["result_shown"] is False
        and state["message"] == ""
    ):
        print("Press and get state backspace \033[92mPASSED\033[0m")
    else:
        print("Press and get state backspace \033[91mFAILED\033[0m")
        all_passed = False

    # Press and get state error

    calculator.clear()
    calculator.press("1")
    calculator.press("/")
    calculator.press("0")

    state = calculator.press_and_get_state("=")

    if (
        state["expression"] == ""
        and state["display"] == ""
        and state["result_shown"] is False
        and state["message"] == "Error: Cannot divide by zero"
    ):
        print("Press and get state error \033[92mPASSED\033[0m")
    else:
        print("Press and get state error \033[91mFAILED\033[0m")
        all_passed = False

    print()

    if all_passed:
        print("ALL TESTS \033[92mPASSED\033[0m")
    else:
        print("SOME TESTS \033[91mFAILED\033[0m")


    # Press operator after result test

    calculator.clear()
    calculator.press("1")
    calculator.press("+")
    calculator.press("2")
    calculator.press_equals()

    state = calculator.press_and_get_state("<")

    if (
            state["expression"] == ""
            and state["display"] == ""
            and state["result_shown"] is False
            and state["message"] == ""
    ):
        print("Backspace after result \033[92mPASSED\033[0m")
    else:
        print("Backspace after result \033[91mFAILED\033[0m")
        all_passed = False

    # Clear after result test

    calculator.clear()
    calculator.press("1")
    calculator.press("+")
    calculator.press("2")
    calculator.press_equals()

    state = calculator.press_and_get_state("C")

    if (
        state["expression"] == ""
        and state["display"] == ""
        and state["result_shown"] is False
        and state["message"] == ""
    ):
        print("Clear after result \033[92mPASSED\033[0m")
    else:
        print("Clear after result \033[91mFAILED\033[0m")
        all_passed = False

    # Negative result through buttons test

    calculator.clear()
    calculator.press("1")
    calculator.press("-")
    calculator.press("2")

    state = calculator.press_and_get_state("=")

    if (
        state["expression"] == "-1"
        and state["display"] == "-1 (-1.0)"
        and state["result_shown"] is True
        and state["message"] == "Result: -1 (-1.0)"
    ):
        print("Negative result through buttons \033[92mPASSED\033[0m")
    else:
        print("Negative result through buttons \033[91mFAILED\033[0m")
        all_passed = False

    # Negative fraction result test

    calculator.clear()
    calculator.press("1")
    calculator.press("/")
    calculator.press("2")
    calculator.press("-")
    calculator.press("3")
    calculator.press("/")
    calculator.press("4")

    state = calculator.press_and_get_state("=")

    if (
        state["expression"] == "-1/4"
        and state["display"] == "-1/4 (-0.25)"
        and state["result_shown"] is True
        and state["message"] == "Result: -1/4 (-0.25)"
    ):
        print("Negative fraction result \033[92mPASSED\033[0m")
    else:
        print("Negative fraction result \033[91mFAILED\033[0m")
        all_passed = False

    # Negative mixed number test

    calculator.clear()
    calculator.press("-")
    calculator.press("1")
    calculator.press(" ")
    calculator.press("1")
    calculator.press("/")
    calculator.press("2")
    calculator.press("+")
    calculator.press("2")

    state = calculator.press_and_get_state("=")

    if (
        state["expression"] == "1/2"
        and state["display"] == "1/2 (0.5)"
        and state["result_shown"] is True
        and state["message"] == "Result: 1/2 (0.5)"
    ):
        print("Negative mixed number \033[92mPASSED\033[0m")
    else:
        print("Negative mixed number \033[91mFAILED\033[0m")
        all_passed = False


    # Division by negative fraction test

    calculator.clear()
    calculator.press("3")
    calculator.press("/")
    calculator.press("4")
    calculator.press("/")
    calculator.press("-")
    calculator.press("1")
    calculator.press("/")
    calculator.press("2")

    state = calculator.press_and_get_state("=")

    if (
        state["expression"] == "-3/2"
        and state["display"] == "-1 1/2 (-1.5)"
        and state["result_shown"] is True
        and state["message"] == "Result: -1 1/2 (-1.5)"
    ):
        print("Division by negative fraction \033[92mPASSED\033[0m")
    else:
        print("Division by negative fraction \033[91mFAILED\033[0m")
        all_passed = False




if __name__ == "__main__":
    run_tests()