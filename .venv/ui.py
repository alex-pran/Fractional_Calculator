import tkinter as tk


root = tk.Tk()
root.title("Fractional Calculator")
root.geometry("500x600")


# =========================
# ДАННЫЕ КАЛЬКУЛЯТОРА
# =========================

main_number = ""
numerator = ""
denominator = ""


# =========================
# ГЛАВНЫЙ ЭКРАН
# =========================

display_frame = tk.Frame(root)

display_frame.pack(
    fill="x",
    padx=10,
    pady=20
)


# Основное значение слева

main_display = tk.Label(
    display_frame,
    text="0",
    font=("Arial", 28),
    anchor="e"
)

main_display.pack(
    side="left",
    pady=(22, 0)
)


# Дробь справа

fraction_display = tk.Frame(display_frame)

fraction_display.pack(
    side="left",
    padx=2
)


# Числитель

numerator_display = tk.Label(
    fraction_display,
    text="",
    font=("Arial", 22)
)

numerator_display.pack()


# Линия дроби

display_line = tk.Frame(
    fraction_display,
    height=2,
    width=70,
    bg="black"
)

display_line.pack(
    fill="x"
)


# Знаменатель

denominator_display = tk.Label(
    fraction_display,
    text="",
    font=("Arial", 22)
)

denominator_display.pack()


# =========================
# ОБНОВЛЕНИЕ ДИСПЛЕЯ
# =========================

def update_display():

    main_display.config(
        text=main_number if main_number else "0"
    )

    numerator_display.config(
        text=numerator
    )

    denominator_display.config(
        text=denominator
    )


# =========================
# ОСНОВНОЕ ЧИСЛО
# =========================

def add_main_number(number):

    global main_number

    if len(main_number) < 10:

        main_number += number

        update_display()


# =========================
# ЧИСЛИТЕЛЬ
# =========================

def add_numerator(number):

    global numerator

    if len(numerator) < 10:

        numerator += number

        update_display()


# =========================
# ЗНАМЕНАТЕЛЬ
# =========================

def add_denominator(number):

    global denominator

    if len(denominator) < 10:

        denominator += number

        update_display()


# =========================
# ОСНОВНАЯ ОБЛАСТЬ
# =========================

main_frame = tk.Frame(root)

main_frame.pack(
    padx=10,
    pady=10
)


# ==================================================
# ЛЕВАЯ ЧАСТЬ — ОСНОВНАЯ КЛАВИАТУРА
# ==================================================

main_keyboard = tk.Frame(main_frame)

main_keyboard.grid(
    row=0,
    column=0,
    padx=20
)


main_digits = [
    ("1", 0, 0),
    ("2", 0, 1),
    ("3", 1, 0),
    ("4", 1, 1),
    ("5", 2, 0),
    ("6", 2, 1),
    ("7", 3, 0),
    ("8", 3, 1),
    ("9", 4, 0),
    ("0", 4, 1)
]


for number, row, column in main_digits:

    button = tk.Button(
        main_keyboard,
        text=number,
        font=("Arial", 20),
        width=3,
        height=1,
        command=lambda n=number: add_main_number(n)
    )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5
    )


# ==================================================
# ПРАВАЯ ЧАСТЬ — ДРОБЬ
# ==================================================

fraction_frame = tk.Frame(main_frame)

fraction_frame.grid(
    row=0,
    column=1,
    padx=20
)


# ==================================================
# ЧИСЛИТЕЛЬ
# ==================================================

numerator_label = tk.Label(
    fraction_frame,
    text="Числитель",
    font=("Arial", 12)
)

numerator_label.pack()


numerator_keyboard = tk.Frame(fraction_frame)

numerator_keyboard.pack(
    pady=5
)


numerator_digits = [
    ("1", 0, 0),
    ("2", 0, 1),
    ("3", 0, 2),
    ("4", 0, 3),
    ("5", 0, 4),
    ("6", 1, 0),
    ("7", 1, 1),
    ("8", 1, 2),
    ("9", 1, 3),
    ("0", 1, 4)
]


for number, row, column in numerator_digits:

    button = tk.Button(
        numerator_keyboard,
        text=number,
        font=("Arial", 16),
        width=2,
        command=lambda n=number: add_numerator(n)
    )

    button.grid(
        row=row,
        column=column,
        padx=2,
        pady=2
    )


# ==================================================
# ЛИНИЯ МЕЖДУ КЛАВИАТУРАМИ
# ==================================================

fraction_line = tk.Frame(
    fraction_frame,
    height=3,
    width=180,
    bg="black"
)

fraction_line.pack(
    fill="x",
    pady=8
)


# ==================================================
# ЗНАМЕНАТЕЛЬ
# ==================================================

denominator_label = tk.Label(
    fraction_frame,
    text="Знаменатель",
    font=("Arial", 12)
)

denominator_label.pack()


denominator_keyboard = tk.Frame(fraction_frame)

denominator_keyboard.pack(
    pady=5
)


denominator_digits = [
    ("1", 0, 0),
    ("2", 0, 1),
    ("3", 0, 2),
    ("4", 0, 3),
    ("5", 0, 4),
    ("6", 1, 0),
    ("7", 1, 1),
    ("8", 1, 2),
    ("9", 1, 3),
    ("0", 1, 4)
]


for number, row, column in denominator_digits:

    button = tk.Button(
        denominator_keyboard,
        text=number,
        font=("Arial", 16),
        width=2,
        command=lambda n=number: add_denominator(n)
    )

    button.grid(
        row=row,
        column=column,
        padx=2,
        pady=2
    )


# =========================
# ЗАПУСК
# =========================

root.mainloop()