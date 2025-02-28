from customtkinter import *
from presentation.about.left_page import *
from tkinter import * 
from presentation.about.component.card_content import *


def show_about_page(about_page_root,left_frmae,right_top_frmae,right_frmae,right_middle_frmae):

    


    left_frame = CTkFrame(about_page_root,corner_radius=10, fg_color="transparent")
    left_frame.pack(side=LEFT, fill=BOTH,padx=10,pady=10)

    left_child_frame = CTkFrame(left_frame,corner_radius=10)
    left_child_frame.pack( fill=BOTH,expand=True,padx=10,pady=10)


    right_frame = CTkFrame(about_page_root,corner_radius=10, fg_color="transparent")
    right_frame.pack(side=RIGHT, fill=BOTH,expand=True,padx=10,pady=10)



    scrollable_frame = CTkScrollableFrame(right_frame,fg_color="transparent")
    scrollable_frame.pack(fill="both", expand=True, padx=10, pady=10)

    right_child_gr_frame = CTkTabview(scrollable_frame)
    right_child_gr_frame.pack(fill=BOTH,expand=True,padx=10,pady=10)

    tab_gr_1 = right_child_gr_frame.add("MFEI")
    tab_gr_2 = right_child_gr_frame.add("GGMI")

    right_child_fe_frame = CTkTabview(scrollable_frame)
    right_child_fe_frame.pack(fill=BOTH,expand=True,padx=10,pady=10)

    tab_fe_1 = right_child_fe_frame.add("HOG")
    tab_fe_2 = right_child_fe_frame.add("GLCM")

    right_child_clv_frame = CTkTabview(scrollable_frame)
    right_child_clv_frame.pack(fill=BOTH,expand=True,padx=10,pady=10)

    tab_clv_1 = right_child_clv_frame.add("K-NN")
    tab_clv_2 = right_child_clv_frame.add("SVM")






    
    left_page_display(left_frame,left_child_frame,left_frmae,right_top_frmae,right_frmae,about_page_root,right_middle_frmae)
    card_method_content(tab_gr_1,"MFEI","Motion Flow Energy Image","Motion Flow Energy Image (MFEI) adalah metode ekstraksi fitur yang digunakan untuk mengidentifikasi objek dalam gambar atau video. HOG menghitung gradien arah dan magnitudo dari piksel dalam gambar. HOG digunakan dalam berbagai aplikasi penglihatan komputer, seperti deteksi wajah, deteksi orang, dan pengenalan karakter.")
    card_method_content(tab_gr_2,"GGMI","Gait Gradient Magnitude Image","Gait Gradient Magnitude Image (GGMI) adalah metode ekstraksi fitur yang digunakan untuk mengidentifikasi objek dalam gambar atau video. HOG menghitung gradien arah dan magnitudo dari piksel dalam gambar. HOG digunakan dalam berbagai aplikasi penglihatan komputer, seperti deteksi wajah, deteksi orang, dan pengenalan karakter.")

    card_method_content(tab_fe_1,"HOG","Support Vector Machine","Histogram of Oriented Gradient (HOG) adalah metode ekstraksi fitur yang digunakan untuk mengidentifikasi objek dalam gambar atau video. HOG menghitung gradien arah dan magnitudo dari piksel dalam gambar. HOG digunakan dalam berbagai aplikasi penglihatan komputer, seperti deteksi wajah, deteksi orang, dan pengenalan karakter.")
    card_method_content(tab_fe_2,"GLCM","Gray Level Co-Occurance Matrix","Gray Level Co-Occurance Matrix (GLCM) adalah metode ekstraksi fitur yang digunakan untuk mengidentifikasi objek dalam gambar atau video. HOG menghitung gradien arah dan magnitudo dari piksel dalam gambar. HOG digunakan dalam berbagai aplikasi penglihatan komputer, seperti deteksi wajah, deteksi orang, dan pengenalan karakter.")

    card_method_content(tab_clv_1,"K-NN","K-Nearest Neighbour","K-Nearest Neighbour (K-NN) adalah metode ekstraksi fitur yang digunakan untuk mengidentifikasi objek dalam gambar atau video. HOG menghitung gradien arah dan magnitudo dari piksel dalam gambar. HOG digunakan dalam berbagai aplikasi penglihatan komputer, seperti deteksi wajah, deteksi orang, dan pengenalan karakter.")
    card_method_content(tab_clv_2,"SVM","Support Vector Machine","Support Vector Machine (SVM) adalah metode ekstraksi fitur yang digunakan untuk mengidentifikasi objek dalam gambar atau video. HOG menghitung gradien arah dan magnitudo dari piksel dalam gambar. HOG digunakan dalam berbagai aplikasi penglihatan komputer, seperti deteksi wajah, deteksi orang, dan pengenalan karakter.")


    
