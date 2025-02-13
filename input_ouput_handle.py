import tkinter as tk
from tkinter import filedialog
import os
import cv2
import shutil
from display_gait import display_video
from utils.config import set_video_state
from utils.custom_button import CustomButton
from utils.displayed_result_image import stop_animation
from utils.widget_check_remover import check_and_remove_widget
from customtkinter import *



def load_images_from_folder(folder_path):
    images = []
    if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    for filename in os.listdir(folder_path):
        img_path = os.path.join(folder_path, filename)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is not None:
            images.append(img)
    return images



def remove_and_clear_display_gait(root,widget_id):
    if os.path.exists("uploads"):
            for filename in os.listdir("uploads"):
                file_path = os.path.join("uploads", filename)
                os.remove(file_path)
            os.rmdir("uploads")

    check_and_remove_widget(root, widget_id)



def create_directory_button(root,second_root, canvas_id,mfei_res_id,text,frame_input_file_idx,gr_animated_id,label_id):
    path_frame = CTkEntry(root, width=450, placeholder_text="Enter the path of the folder")
    path_frame.pack(side=LEFT,pady=10,padx=10)
    def choose_directory():

        
        set_video_state(True)
        remove_and_clear_display_gait(second_root,label_id.get())   
        # menghapus canvas yang sudah ada
        remove_and_clear_display_gait(second_root,canvas_id.get())

        remove_and_clear_display_gait(second_root,mfei_res_id.get())

        remove_and_clear_display_gait(second_root,gr_animated_id.get())
        

        # mengecek direktory secara keseluruhan
        directory = filedialog.askdirectory()
        path_frame.configure(placeholder_text=directory)
        if directory:
           
            uploads_dir = os.path.join(os.getcwd(), "uploads")

            if not os.path.exists(uploads_dir):
                os.makedirs(uploads_dir)
            
            image_files = [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
            
            for img in image_files:
                
                img_src = os.path.join(directory, img)
                
                new_img_path = os.path.join(uploads_dir, img)
             
                shutil.copy(img_src, new_img_path)
        
        def count_files_in_directory(directory):
            return len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])



        directory_path = "uploads"
        num_files = count_files_in_directory(directory_path)
      

        if(num_files > 0):
            print("Displaying video...")
            display_video(second_root, canvas_id,"uploads",frame_input_file_idx)


    
    
   
    path_button_frame = CTkButton(root, text="Choose Frame Folder",command=choose_directory)
    path_button_frame.pack(side=RIGHT,pady=10,padx=10)
    # return CustomButton(root, text, choose_directory)
    return path_button_frame


def remove_folder(root,display_root,canvas_id,folder_path, mfei_res_id,gr_animated_id,label_id):
    def remove():

        stop_animation()
        remove_and_clear_display_gait(display_root,label_id.get())        
        remove_and_clear_display_gait(display_root,canvas_id.get())
        remove_and_clear_display_gait(display_root,mfei_res_id.get())
        remove_and_clear_display_gait(display_root,gr_animated_id.get())

        # Hapus folder dan isinya
        if os.path.exists(folder_path):
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                os.remove(file_path)
            os.rmdir(folder_path)

    return CustomButton(root, "Remove data", remove,"danger")


def create_video_from_frames(frame_folder, output_video_path, fps=20):
    # Dapatkan daftar file frame dan urutkan
    frames = [f for f in os.listdir(frame_folder) if f.endswith('.png') or f.endswith('.jpg')]
    frames.sort()

    # Baca frame pertama untuk mendapatkan ukuran video
    first_frame_path = os.path.join(frame_folder, frames[0])
    first_frame = cv2.imread(first_frame_path)
    height, width, layers = first_frame.shape

    # Tentukan codec dan buat VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec untuk format .mp4
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # Tulis setiap frame ke video
    for frame_name in frames:
        frame_path = os.path.join(frame_folder, frame_name)
        frame = cv2.imread(frame_path)
        video_writer.write(frame)

    # Selesai menulis video
    video_writer.release()
    print(f"Video saved to {output_video_path}")


def extract_frames_from_video(video_path, output_folder):
    # Buat folder output jika belum ada

    os.makedirs(output_folder, exist_ok=True)

    # Buka video
    video_capture = cv2.VideoCapture(video_path)

    # Periksa apakah video berhasil dibuka
    if not video_capture.isOpened():
        message = f"Error: Tidak dapat membuka video {video_path}"
        return message

    frame_count = 0
    while True:
        # Baca frame dari video
        ret, frame = video_capture.read()

        # Jika tidak ada frame lagi, keluar dari loop
        if not ret:
            break

        # Simpan frame sebagai gambar
        frame_filename = os.path.join(output_folder, f"{frame_count:04d}.png")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    # Selesai memproses video
    video_capture.release()
    return f"Extracted {frame_count} frames to {output_folder}"


def check_input_video(request,app):
    if request.method == "POST":
        if "videoInput" not in request.files:
            return 'Is empty file'

        dataVideo = request.files['videoInput']

        if dataVideo.filename == "":
            return 'You not select any video'
        
        if dataVideo:

            file_path = os.path.join(app.config['UPLOAD_FOLDER'], dataVideo.filename)
            dataVideo.save(file_path)
            result = extract_frames_from_video(file_path, "output_frame")
            return f'File  {file_path} and {result}'
        

        
frame_folder = 'E:/kuliah/skripsi/datavideo/casia/fn/fn02/0200' 
# create_video_from_frames(frame_folder, "output_video.mp4")
video_gait = "E:/kuliah/skripsi/code/mfei_method_using_tkinter/output_video.mp4"
# result = extract_frames_from_video(video_gait, "output_frame")