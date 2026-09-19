import tkinter as tk


root = tk.Tk()
root.title("Fractional Calculator")
root.geometry("320x500")


display = tk.Label(
    root,
    text="0",
    font=("Arial", 28),
    anchor="e"
)

display.pack(
    fill="x",
    padx=10,
    pady=20
)


main_frame = tk.Frame(root)

main_frame.pack(
    padx=10,
    pady=10
)


# Клавиатура слева

button_frame = tk.Frame(main_frame)

button_frame.grid(
    row=0,
    column=0,
    padx=10
)


button_1 = tk.Button(
    button_frame,
    text="1",
    font=("Arial", 20)
)
button_1.grid(row=0, column=0, padx=5, pady=5)


button_2 = tk.Button(
    button_frame,
    text="2",
    font=("Arial", 20)
)
button_2.grid(row=0, column=1, padx=5, pady=5)


button_3 = tk.Button(
    button_frame,
    text="3",
    font=("Arial", 20)
)
button_3.grid(row=1, column=0, padx=5, pady=5)


button_4 = tk.Button(
    button_frame,
    text="4",
    font=("Arial", 20)
)
button_4.grid(row=1, column=1, padx=5, pady=5)


button_5 = tk.Button(
    button_frame,
    text="5",
    font=("Arial", 20)
)
button_5.grid(row=2, column=0, padx=5, pady=5)


button_6 = tk.Button(
    button_frame,
    text="6",
    font=("Arial", 20)
)
button_6.grid(row=2, column=1, padx=5, pady=5)


button_7 = tk.Button(
    button_frame,
    text="7",
    font=("Arial", 20)
)
button_7.grid(row=3, column=0, padx=5, pady=5)


button_8 = tk.Button(
    button_frame,
    text="8",
    font=("Arial", 20)
)
button_8.grid(row=3, column=1, padx=5, pady=5)


button_9 = tk.Button(
    button_frame,
    text="9",
    font=("Arial", 20)
)
button_9.grid(row=4, column=0, padx=5, pady=5)


button_0 = tk.Button(
    button_frame,
    text="0",
    font=("Arial", 20)
)
button_0.grid(row=4, column=1, padx=5, pady=5)


# Дробь справа

fraction_frame = tk.Frame(main_frame)

fraction_frame.grid(
    row=0,
    column=1,
    padx=10
)


numerator = tk.Entry(
    fraction_frame,
    font=("Arial", 24),
    width=10,
    justify="center"
)

numerator.insert(0, "0")

numerator.pack()

numerator.pack()


fraction_line = tk.Frame(
    fraction_frame,
    height=2,
    width=180,
    bg="black"
)

fraction_line.pack(
    fill="x",
    pady=3
)


denominator = tk.Entry(
    fraction_frame,
    font=("Arial", 24),
    width=10,
    justify="center"
)

denominator.insert(0, "1")

denominator.pack()

denominator.pack()


root.mainloop()