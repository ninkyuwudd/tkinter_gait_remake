





def check_and_remove_widget(parent, widget_name):
    """Cek apakah widget tertentu ada, dan hapus jika ditemukan."""
    for widget in parent.winfo_children():
        if str(widget) == widget_name:  # Periksa nama widget
            widget.destroy()
            print(f"Widget {widget_name} telah dihapus.")
            return
    print(f"Widget {widget_name} tidak ditemukan.")