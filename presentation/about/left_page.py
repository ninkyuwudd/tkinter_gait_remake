from customtkinter import *

def left_page_display(main_left,main_left_root):
    go_back_to_execute_page_button = CTkButton(main_left, text="<- Go Back", )
    go_back_to_execute_page_button.pack(pady=10, padx=20)

    best_label = CTkLabel(main_left_root, text="BEST F1 SCORE", font=("Helvetica", 15))
    best_label.pack(pady=10)

    title_gr_label = CTkLabel(main_left_root, text="Gait Representation", font=("Helvetica", 10))
    title_gr_label.pack(pady=2)

    gr_label = CTkLabel(main_left_root, text="MFEI", font=("Helvetica", 15, "bold"))
    gr_label.pack(pady=2)

    title_fe_label = CTkLabel(main_left_root, text="Feature Extraction", font=("Helvetica", 10))
    title_fe_label.pack(pady=2)

    fe_label = CTkLabel(main_left_root, text="HOG", font=("Helvetica", 15, "bold"))
    fe_label.pack(pady=2)


    title_model_label = CTkLabel(main_left_root, text="Clasification", font=("Helvetica", 10))
    title_model_label.pack(pady=2)

    model_label = CTkLabel(main_left_root, text="SVC", font=("Helvetica", 15, "bold"))
    model_label.pack(pady=2)



