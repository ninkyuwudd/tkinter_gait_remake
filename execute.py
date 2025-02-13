

import time
from tkinter import ttk
from display_gait import show_ndarray_animation
from input_ouput_handle import load_images_from_folder, remove_folder

import pandas as pd

from method.method_hog import compute_hog
from method.method_mfei import execute_mfei
from method.method_pre_processing import normalize_silhouettes
from method.method_svc import clasification_data
from utils.custom_button import CustomButton
import numpy as np  
import os


from utils.custom_proggress_bar import custom_progress_bar
from utils.displayed_result_image import show_image_on_tkinter
from utils.widget_check_remover import check_and_remove_widget


def executeProccess(root,result_root,mfei_res_id,label_id,gr_animated_id):
    def runProggram():
        

        # check_and_remove_widget(root, label_id.get())
        
        load_images = load_images_from_folder("uploads")
        normalize= normalize_silhouettes(load_images)
        show_ndarray_animation(normalize,result_root,gr_animated_id)
        mfei = execute_mfei(normalize)
        show_image_on_tkinter(result_root,mfei_res_id, mfei)
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
  
        custom_progress_bar(result_root,result,label_id)
 
         
        print(result)
        print("Data has been executed")
        # for filename in os.listdir("uploads"):
        #     file_path = os.path.join("uploads", filename)
        #     os.remove(file_path)
        # os.rmdir("uploads")
        # remove_folder(root,"uploads")
        
    return CustomButton(root, "Execute Data", runProggram,"success")