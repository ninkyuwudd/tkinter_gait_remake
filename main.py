from customtkinter import *
import tkinter as tk
from input_ouput_handle import *
from execute import executeProccess
from input_ouput_handle import *



def main():
    root = CTk()
    root.title("Gait Recognition")
    root.geometry("800x550")
    # root.resizable(False, False)

    left_frmae = CTkFrame(root)
    left_frmae.pack(side=LEFT, fill=BOTH)

    
    right_top_frmae = CTkFrame(root,corner_radius=10, fg_color="transparent")
    right_top_frmae.pack(side=TOP, fill=BOTH)

    right_frmae = CTkFrame(root,corner_radius=10,fg_color="transparent")
    right_frmae.pack(side=BOTTOM, fill=BOTH, expand=True,padx=10,pady=10)

    right_middle_frmae = CTkFrame(root,corner_radius=10, fg_color="transparent")
    right_middle_frmae.pack( fill=BOTH)

     # id untuk menghapus widget
    canvas_id = tk.StringVar()
    label_id = tk.StringVar()
    mfei_res_id = tk.StringVar()
    gr_animated_id = tk.StringVar()
    frame_input_file_idx = 0

 

    menu_label = CTkLabel(left_frmae, text="Menu", font=("Helvetica", 13))
    menu_label.pack(pady=2)


    # Upload sequence data dari folder kita dan menampilkan animasi gaya berjalan
    create_directory_button(right_top_frmae, right_middle_frmae,right_frmae,canvas_id,mfei_res_id,"Choose Directory",frame_input_file_idx,gr_animated_id,label_id)


        # Memproses data yang sudah di upload
    executeProccess(left_frmae,right_frmae,right_middle_frmae,mfei_res_id,label_id,gr_animated_id)

        # menghapus data folder yang sudah di upload
    remove_folder(left_frmae,right_frmae,right_middle_frmae,canvas_id, "uploads", mfei_res_id,gr_animated_id,label_id)


  

    created_by_label = CTkLabel(left_frmae, text="Created By Reihan Wudd H", font=("Helvetica", 10))
    created_by_label.pack(side=BOTTOM,pady=2)

 

    root.mainloop()


if __name__ == "__main__":
    main()