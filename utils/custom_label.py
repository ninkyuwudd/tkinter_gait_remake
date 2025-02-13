



from tkinter import Label, ttk


def custom_label(root,text,label_id):
    our_label = ttk.Label(root, text=text, font=("Helvetica", 15),bootstyle="success")
    our_label.grid(pady=10)
    # label_id.set(our_label)

    