

import time
from tkinter import ttk
from display_gait import show_ndarray_animation
from input_ouput_handle import load_images_from_folder, remove_folder

import pandas as pd
from customtkinter import *
from method.method_hog import compute_hog
from method.method_mfei import execute_mfei
from method.method_ggmi import newGGMIcalculated
from method.method_pre_processing import normalize_silhouettes
from method.method_svc import clasification_data
from utils.custom_button import CustomButton
import numpy as np  
import os


from utils.custom_proggress_bar import custom_progress_bar
from utils.displayed_result_image import show_image_on_tkinter
from utils.widget_check_remover import check_and_remove_widget


def executeProccess(root,result_root,middle_frame,mfei_res_id,label_id,gr_animated_id):
    method_label = CTkLabel(root, text="Method", font=("Helvetica", 13))
    method_label.pack(pady=2)
    dropdown_method = CTkComboBox(root,values=["MFEI","GGMI"],font=("Helvetica", 13))
    dropdown_method.pack(pady=2,padx=10,)
    menu_label = CTkLabel(root, text="Menu", font=("Helvetica", 13))
    menu_label.pack(pady=2)

    def runProggram():
        

        # check_and_remove_widget(root, label_id.get())
        start_time = time.time()  # Catat waktu mulai
        load_images = load_images_from_folder("uploads")
        image_total = len(load_images)
        normalize= normalize_silhouettes(load_images)
        if(dropdown_method.get() == "MFEI"):
            print("this is from mfei")
            mfei = execute_mfei(normalize)
        else:
            mfei = newGGMIcalculated(normalize)
       
        hog = compute_hog(mfei)    
        faltten_hog = np.array(hog).flatten()
        if len(faltten_hog) > 0:
            df = pd.DataFrame([faltten_hog], columns=[f'feature_{i}' for i in range(len(faltten_hog))])
       
            
            # Menyimpan DataFrame ke file CSV
            df.to_csv("input_testing_data.csv", index=False)
            print(f"Hasil disimpan ke: input_testing_data.csv")
        else:
            print(f"Tidak ada data yang diproses")
        result = clasification_data()

        end_time = time.time()  # Catat waktu selesai
        execution_time = end_time - start_time

        show_ndarray_animation(normalize,result_root,gr_animated_id)
        custom_progress_bar(middle_frame,result,label_id,image_total,execution_time)
        show_image_on_tkinter(result_root,mfei_res_id, mfei)
         
        print(result)
        print("Data has been executed")
        # for filename in os.listdir("uploads"):
        #     file_path = os.path.join("uploads", filename)
        #     os.remove(file_path)
        # os.rmdir("uploads")
        # remove_folder(root,"uploads")
        
    return CustomButton(root, "Execute Data", runProggram,"success")