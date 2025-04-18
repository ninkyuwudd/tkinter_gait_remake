



import time
from tkinter import HORIZONTAL
from tkinter import ttk
from tkinter.ttk import Progressbar
import threading
from customtkinter import *

from utils.custom_label import custom_label





def custom_progress_bar(root,text,label_id,image_total,execution_time):
    lbl_frame_result = CTkFrame(root,corner_radius=10)
    lbl_frame_result.pack(side="right",padx=10,pady=10,expand=True,fill="both")
    label_id.set(lbl_frame_result)
    title_label = CTkLabel(lbl_frame_result, text="Recognition Result", font=("Helvetica", 15))
    title_label.pack(padx=10,pady=10)

    


    style = ttk.Style()
    style.configure("Transparent.TLabel", background="black", foreground="white", font=("Helvetica", 15))
    style.configure("Transparent.Horizontal.TProgressbar", background="black", troughcolor="black", borderwidth=0)


    progress_frame = CTkFrame(lbl_frame_result, corner_radius=10)
    progress_frame.pack(padx=10, pady=10, fill=BOTH)

    percent_label = ttk.Label(progress_frame, text=f"{0}%", style="Transparent.TLabel")
    percent_label.pack(side=LEFT, padx=10, pady=10)
    
    proggress_bar = ttk.Progressbar(progress_frame, orient=HORIZONTAL, length=150, mode='determinate', style="Transparent.Horizontal.TProgressbar")
    proggress_bar.pack(side=LEFT, padx=10, pady=10)

    def update_progress():
        for i in range(90):
            proggress_bar['value'] = i
            percent_label['text'] = f"{i+5}%"
            lbl_frame_result.update_idletasks()
            time.sleep(0.001)
        
        time.sleep(1)
        progress_frame.pack_forget()
        # proggress_bar.pack_forget()
        # percent_label.pack_forget()

        # duration_value = "Duration: {:.2f} seconds".format(time)
        # duration = ttk.Label(lbl_frame_result, text=duration_value, font=("Helvetica", 10))
        # duration.grid(pady=10)
        total_image_label = CTkLabel(lbl_frame_result, text=f"Total Frame: {image_total}", font=("Helvetica", 12),anchor="w",justify=LEFT,)
        total_image_label.pack(padx=10, pady=10,fill=BOTH)

        duration_label = CTkLabel(lbl_frame_result, text=f"Duration: {execution_time:.2f} seconds", font=("Helvetica", 12),anchor="w",justify=LEFT,)
        duration_label.pack(padx=10, pady=10,fill=BOTH)

        container = CTkFrame(lbl_frame_result,corner_radius=10)
        container.pack(padx=10, pady=10)
        container_label = CTkLabel(container, text=text, text_color="green",font=("Helvetica", 15),anchor="w",justify=LEFT,)
        container_label.pack(padx=10, pady=10,fill=BOTH)
        # custom_label(lbl_frame_result, text,label_id)
        
    

    threading.Thread(target=update_progress).start()