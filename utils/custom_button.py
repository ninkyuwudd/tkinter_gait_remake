
from tkinter import ttk
from customtkinter import *



# class CustomButton(tk.Button):
#     def __init__(self, master, text, command):
#         super().__init__(master, text=text, command=command)
#         self.grid(pady=10)

def CustomButton(master, text, command, color = "primary"):
    button = CTkButton(master, command=command, text=text)
    button.pack(pady=10,padx=10)
    # button = ttk.Button(master, text=text, command=command,width=20,bootstyle=color)
    # button.grid(pady=10,padx=20)
    # button.config(state=tk.DISABLED)
    return button