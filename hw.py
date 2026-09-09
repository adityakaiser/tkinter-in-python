import tkinter as tk
from tkinter import messagebox

def register_user():
    name = name_entry.get()
    workshop = workshop_var.get()
    
    if name == "":
        messagebox.showwarning("Error", "Please enter your name.")
    else:
        messagebox.showinfo("Success", f"Thank you {name}!\nYou registered for {workshop}.")
        name_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Workshop Sign-Up")
root.geometry("300x200")

tk.Label(root, text="Your Name:").pack(pady=5)
name_entry = tk.Entry(root, width=25)
name_entry.pack(pady=5)

tk.Label(root, text="Select Workshop:").pack(pady=5)
workshops = ["Python Basics", "Pygame Development", "Tkinter GUI Design"]
workshop_var = tk.StringVar(value=workshops[0])
workshop_menu = tk.OptionMenu(root, workshop_var, *workshops)
workshop_menu.pack(pady=5)

submit_button = tk.Button(root, text="Register", command=register_user)
submit_button.pack(pady=15)

root.mainloop()
