from customtkinter import *
from presentation.about.left_page import *
from tkinter import * 


def show_about_page(about_page_root):


    left_frame = CTkFrame(about_page_root,corner_radius=10, fg_color="transparent")
    left_frame.pack(side=LEFT, fill=BOTH,padx=10,pady=10)

    left_child_frame = CTkFrame(left_frame,corner_radius=10)
    left_child_frame.pack( fill=BOTH,expand=True,padx=10,pady=10)


    right_frame = CTkFrame(about_page_root,corner_radius=10, fg_color="transparent")
    right_frame.pack(side=RIGHT, fill=BOTH,expand=True,padx=10,pady=10)



    scrollable_frame = CTkScrollableFrame(right_frame,fg_color="transparent")
    scrollable_frame.pack(fill="both", expand=True, padx=10, pady=10)

    right_child_gr_frame = CTkTabview(scrollable_frame)
    right_child_gr_frame.pack(fill=BOTH,expand=True,padx=10,pady=10)

    tab_gr_1 = right_child_gr_frame.add("MFEI")
    tab_gr_2 = right_child_gr_frame.add("GGMI")

    right_child_fe_frame = CTkTabview(scrollable_frame)
    right_child_fe_frame.pack(fill=BOTH,expand=True,padx=10,pady=10)

    tab_fe_1 = right_child_fe_frame.add("HOG")
    tab_fe_2 = right_child_fe_frame.add("GLCM")

    right_child_clv_frame = CTkTabview(scrollable_frame)
    right_child_clv_frame.pack(fill=BOTH,expand=True,padx=10,pady=10)

    tab_clv_1 = right_child_clv_frame.add("K-NN")
    tab_clv_2 = right_child_clv_frame.add("SVM")

    



    left_page_display(left_frame,left_child_frame)


    
