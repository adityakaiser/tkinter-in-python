import tkinter as tk
from tkinter import messagebox

CORRECT_PIN = "1234"
current_pin = ""

def add_digit(digit):
    global current_pin
    if len(current_pin) < 4:
        current_pin += digit
        pin_label.config(text="*" * len(current_pin))

def press_1(): add_digit("1")
def press_2(): add_digit("2")
def press_3(): add_digit("3")
def press_4(): add_digit("4")
def press_5(): add_digit("5")
def press_6(): add_digit("6")
def press_7(): add_digit("7")
def press_8(): add_digit("8")
def press_9(): add_digit("9")
def press_0(): add_digit("0")

def clear_pin():
    global current_pin
    current_pin = ""
    pin_label.config(text="")

def submit_pin():
    global current_pin
    if current_pin == CORRECT_PIN:
        messagebox.showinfo("Success", "PIN Correct!\nAccess Granted.")
    else:
        messagebox.showerror("Error", "Incorrect PIN!\nTry Again.")
    clear_pin()

root = tk.Tk()
root.title("ATM")
root.geometry("250x350")

pin_label = tk.Label(root, text="", font=("Arial", 24), bg="white", width=10, relief="sunken")
pin_label.pack(pady=20)

grid_frame = tk.Frame(root)
grid_frame.pack()

tk.Button(grid_frame, text="1", font=("Arial", 14), width=4, height=2, command=press_1).grid(row=0, column=0, padx=5, pady=5)
tk.Button(grid_frame, text="2", font=("Arial", 14), width=4, height=2, command=press_2).grid(row=0, column=1, padx=5, pady=5)
tk.Button(grid_frame, text="3", font=("Arial", 14), width=4, height=2, command=press_3).grid(row=0, column=2, padx=5, pady=5)

tk.Button(grid_frame, text="4", font=("Arial", 14), width=4, height=2, command=press_4).grid(row=1, column=0, padx=5, pady=5)
tk.Button(grid_frame, text="5", font=("Arial", 14), width=4, height=2, command=press_5).grid(row=1, column=1, padx=5, pady=5)
tk.Button(grid_frame, text="6", font=("Arial", 14), width=4, height=2, command=press_6).grid(row=1, column=2, padx=5, pady=5)

tk.Button(grid_frame, text="7", font=("Arial", 14), width=4, height=2, command=press_7).grid(row=2, column=0, padx=5, pady=5)
tk.Button(grid_frame, text="8", font=("Arial", 14), width=4, height=2, command=press_8).grid(row=2, column=1, padx=5, pady=5)
tk.Button(grid_frame, text="9", font=("Arial", 14), width=4, height=2, command=press_9).grid(row=2, column=2, padx=5, pady=5)

tk.Button(grid_frame, text="Clear", font=("Arial", 10), width=4, height=2, bg="yellow", command=clear_pin).grid(row=3, column=0, padx=5, pady=5)
tk.Button(grid_frame, text="0", font=("Arial", 14), width=4, height=2, command=press_0).grid(row=3, column=1, padx=5, pady=5)
tk.Button(grid_frame, text="Enter", font=("Arial", 10), width=4, height=2, bg="green", command=submit_pin).grid(row=3, column=2, padx=5, pady=5)

root.mainloop()
#coorect pin is 1234