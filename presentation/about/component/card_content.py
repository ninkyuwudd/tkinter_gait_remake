from customtkinter import *

def card_method_content(main_root,title,title_long,description):

    left_card_frame = CTkFrame(main_root,corner_radius=10, fg_color="transparent")
    left_card_frame.pack(side=LEFT, fill=BOTH,padx=10,pady=10,expand=False)

    right_card_frame = CTkFrame(main_root,corner_radius=10, fg_color="transparent")
    right_card_frame.pack(side=RIGHT, fill=BOTH,padx=10,pady=10,expand=True)

    big_method_label = CTkLabel(left_card_frame, text=title, font=("Helvetica", 18))
    big_method_label.pack(pady=2)

    method_label = CTkLabel(right_card_frame, text=title_long, font=("Helvetica", 15,),anchor="w",justify=LEFT,)
    method_label.pack(pady=2,fill="both")

    detail_method_label = CTkLabel(right_card_frame, text=description, font=("Helvetica", 10),wraplength=300,anchor="w",justify=LEFT)
    detail_method_label.pack(pady=2,fill="both")
