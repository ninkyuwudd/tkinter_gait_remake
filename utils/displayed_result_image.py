
from tkinter import Label, PanedWindow
from tkinter import ttk
from tkinter.ttk import Labelframe
from PIL import Image, ImageTk
from customtkinter import *

from utils.config import set_video_state

def show_image_on_tkinter(root,mfei_res_id, image_array):



    lbl_frame = CTkFrame(root)
    lbl_frame.pack(side="right",padx=10,pady=10,expand=True,fill="both")
    mfei_res_id.set(lbl_frame)

    title_label = CTkLabel(lbl_frame, text="MFEI Result", font=("Helvetica", 15))
    title_label.pack(padx=10,pady=10)


    # gr_.set(lbl_frame_result)


    print(mfei_res_id.get(), "from mfei")

    image = Image.fromarray(image_array)

    # Konversi Image ke PhotoImage
    photo = ImageTk.PhotoImage(image)

    # Tampilkan gambar di tkinter menggunakan Label
    label = Label(lbl_frame, image=photo)
    label.image = photo  # Simpan referensi agar gambar tidak hilang
    label.pack()
  


def stop_animation():

    set_video_state(False)

 