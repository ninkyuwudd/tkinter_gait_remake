import os
from tkinter import Canvas, PanedWindow
from tkinter import ttk
from tkinter.ttk import Labelframe
from PIL import Image, ImageTk
import cv2
import tkinter as tk
from customtkinter import *

from utils.config import get_video_state



def play_video_from_frames(frame_folder, canvas, root, frame_input_file_idx, delay=35):
    """Play video from frame sequence stored in a folder."""
    # Get all frame filenames and sort numerically
    frame_files = sorted(os.listdir(frame_folder), key=lambda x: int(x.split('.')[0]))

    
    def update_frame():
        nonlocal frame_input_file_idx
        # stop_input_file_animation 
        is_animation_running = get_video_state()
        if not is_animation_running:
            print("image videor frame stop....")
            return
        
        # Loop through frames
        if frame_input_file_idx < len(frame_files) :
            frame_path = os.path.join(frame_folder, frame_files[frame_input_file_idx])
            frame = cv2.imread(frame_path)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Convert to ImageTk format for Tkinter display
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            
            # Display the frame on the canvas
            canvas.image = imgtk  # Keep reference to avoid garbage collection
            canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
            
            frame_input_file_idx += 1
        else:
            frame_input_file_idx = 0  # Restart the video loop
 
        root.after(delay, update_frame)  # Schedule the next frame
            
    update_frame()


def display_video(root, canvas_id,frame_folder,frame_input_file_idx):


    # lbl_frame = Labelframe(root,text="Input Gait")
    lbl_frame = CTkFrame(root,corner_radius=10)
    lbl_frame.pack(side=LEFT,padx=10, pady=10,expand=True,fill="both")
    canvas_id.set(lbl_frame)

    lbl_title = CTkLabel(lbl_frame, text="Input Gait", font=("Helvetica", 15))
    lbl_title.pack(padx=10,pady=10)



    first_frame = cv2.imread(os.path.join(frame_folder, sorted(os.listdir(frame_folder))[0]))
    height, width, _ = first_frame.shape

    canvas = Canvas(lbl_frame, width=width - 20, height=height - 20, bg='black')

    canvas.pack()


    # Play video
    play_video_from_frames(frame_folder, canvas, root,frame_input_file_idx)




def display_ndarray_frames_in_sequence(root, canvas, frames, delay=33):
    """
    Menampilkan urutan frame pada canvas sebagai animasi.
    
    Args:
        root: Tkinter root window.
        canvas: Tkinter Canvas widget.
        frames: List of numpy.ndarray (grayscale images).
        delay: Waktu delay antar frame dalam milidetik (default 100 ms).
    """
    idx = 0
    def update_frame():

        nonlocal idx

        if idx < len(frames):
            # Konversi frame numpy.ndarray ke format Tkinter (ImageTk)
            frame = frames[idx]
            img = ImageTk.PhotoImage(Image.fromarray(frame).convert("L"))
            
            # Perbarui canvas dengan gambar baru
            canvas.image = img  # Simpan referensi ke gambar
            canvas.create_image(0, 0, anchor=tk.NW, image=img)
            
  
            idx += 1
        else:
            idx = 0
        
        root.after(delay, update_frame)

    # Mulai menampilkan frame dari indeks pertama
    update_frame()

def show_ndarray_animation(aligned_frames,root,gr_animated_id):
        #     label = ttk.Label(result_root, text="", font=("Helvetica", 10))
        # label.grid(row=1,column=0) 

    lbl_frame = CTkFrame(root)
    lbl_frame.pack(side=LEFT,padx=10,pady=10,expand=True,fill="both")
    gr_animated_id.set(lbl_frame)

    lbl_title = CTkLabel(lbl_frame, text="After Normalization", font=("Helvetica", 15))
    lbl_title.pack(padx=10,pady=10)

    
    # Asumsi semua frame memiliki ukuran yang sama
    frame_height, frame_width = aligned_frames[0].shape
    
    # Membuat canvas dengan ukuran sesuai frame
    canvas = tk.Canvas(lbl_frame, width=frame_width, height=frame_height)
    # lbl_frame.add(canvas)
    canvas.pack()
    
    # Menampilkan animasi
    display_ndarray_frames_in_sequence(lbl_frame, canvas, aligned_frames, delay=35)