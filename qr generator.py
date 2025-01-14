import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
def generate_qr_code():
    link = entry.get()
    if not link:
        messagebox.showerror("Error", "Please enter a link")
        return
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white').convert("RGB")
    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk
    img_width, img_height = img.size
    window_width = max(400, img_width + 40)
    window_height = img_height + 160
    center_window(root, window_width, window_height)
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')
root = tk.Tk()
root.title("QR Code Generator")
initial_width = 400
initial_height = 300
center_window(root, initial_width, initial_height)
entry_label = tk.Label(root, text="Enter the link:")
entry_label.pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=20)
qr_label = tk.Label(root)
qr_label.pack(pady=10)
root.mainloop()