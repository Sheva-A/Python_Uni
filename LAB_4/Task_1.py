import tkinter as tk
from tkinter import messagebox

allowed_chars = set('0123456789+-*/.() ')


def button_click(char):
    entry.insert(tk.END, char)


def clear():
    entry.delete(0, tk.END)


def calculate():
    expr = entry.get()
    if all(char in allowed_chars for char in expr):
        try:
            result = eval(expr)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except ZeroDivisionError:
            messagebox.showerror("Помилка", "Ділення на нуль.")
            clear()
        except Exception:
            messagebox.showerror("Помилка", "Некоректний вираз.")
            clear()
    else:
        messagebox.showerror("Помилка", "Вираз містить недопустимі символи.")
        clear()


root = tk.Tk()
root.title("Калькулятор")
root.geometry("320x420")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

row = 1
col = 0

for btn in buttons:
    if btn == '=':
        tk.Button(root, text=btn, width=7, height=2, command=calculate).grid(row=row, column=col, pady=5)
    elif btn == 'C':
        tk.Button(root, text=btn, width=32, height=2, command=clear).grid(row=5, column=0, columnspan=4, pady=5)
    else:
        tk.Button(root, text=btn, width=7, height=2, command=lambda b=btn: button_click(b)).grid(row=row, column=col,
                                                                                                 pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
