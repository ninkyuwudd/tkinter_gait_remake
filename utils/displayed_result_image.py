
from tkinter import Label, PanedWindow
from tkinter import ttk
from tkinter.ttk import Labelframe
from PIL import Image, ImageTk

from utils.config import set_video_state

def show_image_on_tkinter(root,mfei_res_id, image_array):



    lbl_frame = ttk.Labelframe(root,text="MFEI Result")
    lbl_frame.grid(row=2,column=1,padx=10,pady=10)
    mfei_res_id.set(lbl_frame)


    # gr_.set(lbl_frame_result)


    print(mfei_res_id.get(), "from mfei")

    image = Image.fromarray(image_array)

    # Konversi Image ke PhotoImage
    photo = ImageTk.PhotoImage(image)

    # Tampilkan gambar di tkinter menggunakan Label
    label = Label(lbl_frame, image=photo)
    label.image = photo  # Simpan referensi agar gambar tidak hilang
    label.grid()
  


def stop_animation():

    set_video_state(False)

 