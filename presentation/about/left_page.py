from customtkinter import *


def goBackMainPage(about_page_root,left_frmae,right_top_frmae,right_frmae,right_middle_frmae):
    about_page_root.pack_forget()
 
    left_frmae.pack(side=LEFT, fill=BOTH)

    right_top_frmae.pack(side=TOP, fill=BOTH)

    right_frmae.pack(side=BOTTOM, fill=BOTH, expand=True,padx=10,pady=10)

    right_middle_frmae.pack( fill=BOTH)


def left_page_display(main_left,main_left_root,left_frmae,right_top_frmae,right_frmae,about_page_root,right_middle_frmae):
    go_back_to_execute_page_button = CTkButton(main_left, text="<- Go Back",command=lambda: goBackMainPage(about_page_root,left_frmae,right_top_frmae,right_frmae,right_middle_frmae))
    go_back_to_execute_page_button.pack(pady=10, padx=20)

    best_label = CTkLabel(main_left_root, text="BEST F1 SCORE", font=("Helvetica", 15))
    best_label.pack(pady=10)

    title_gr_label = CTkLabel(main_left_root, text="Gait Representation", font=("Helvetica", 10),anchor="w",justify=LEFT,)
    title_gr_label.pack(pady=2,fill=BOTH,padx=20)

    gr_label = CTkLabel(main_left_root, text="MFEI", font=("Helvetica", 15, "bold"),anchor="w",justify=LEFT,)
    gr_label.pack(pady=2,fill=BOTH,padx=20)

    title_fe_label = CTkLabel(main_left_root, text="Feature Extraction", font=("Helvetica", 10),anchor="w",justify=LEFT,)
    title_fe_label.pack(pady=2,fill=BOTH,padx=20)

    fe_label = CTkLabel(main_left_root, text="HOG", font=("Helvetica", 15, "bold"),anchor="w",justify=LEFT,)
    fe_label.pack(pady=2,fill=BOTH,padx=20)


    title_model_label = CTkLabel(main_left_root, text="Clasification", font=("Helvetica", 10),anchor="w",justify=LEFT,)
    title_model_label.pack(pady=2,fill=BOTH,padx=20)

    model_label = CTkLabel(main_left_root, text="SVC", font=("Helvetica", 15, "bold"),anchor="w",justify=LEFT,)
    model_label.pack(pady=2,fill=BOTH,padx=20)



