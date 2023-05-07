#Import the math
import math

#library
import cv2
import numpy as np

from PIL import Image
from PIL import ImageTk


#user interface
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

#local module
import detect



# Khởi tạo cửa sổ
root = tk.Tk()
root.title("Lưới 2x2")

# Cài đặt kích thước cửa sổ
root.geometry("900x600")

# Tạo frame để chứa lưới 2x2
frame_grid = ttk.Frame(root, padding=10)
frame_grid.grid(row=0, column=0)

images = []
for i in range(4):
    filename = f"./anh/skeleton.png"
    image = Image.open(filename)
    image = image.resize((200, 200), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    images.append(photo)
    label = ttk.Label(frame_grid, image=photo)
    label.grid(row=i//2, column=i%2, padx=10, pady=10)


# Tạo frame để chứa các button bên phải
frame_buttons = ttk.Frame(root, padding=10)
frame_buttons.grid(row=0, column=1, sticky="n")


def load_results():
    images = []
    for i in range(4):
        filename = f"./anh/{i+1}.png"
        image = Image.open(filename)
        image = image.resize((200, 200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        images.append(photo)
        label = ttk.Label(frame_grid, image=photo)
        label.grid(row=i//2, column=i%2, padx=10, pady=10)


def run():
    file_path = filedialog.askopenfilename(title="Open Image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    if file_path:
        #xu ly anh ngay day
        detect.detect(file_path)
        
    
# Tạo các button và thêm vào frames
importFileButton = ttk.Button(frame_buttons, text="Select File", command=run)
importFileButton.grid(row=1, column=0, pady=20, padx=20)

resultLabel = ttk.Label(frame_buttons, text="Result")
resultLabel.grid(row=2, column=0, pady=0, padx=20)
resultValue = ttk.Label(frame_buttons, text="18N6038")
resultValue.grid(row=3, column=0, pady=0, padx=20)

refreshButton = ttk.Button(frame_buttons, text="Refresh")
refreshButton.grid(row=4, column=0, pady=15, padx=20)

exitButton = ttk.Button(frame_buttons, text="Exit")
exitButton.grid(row=5, column=0, pady=10, padx=20)

# Tạo các ảnh và thêm vào lưới 2x2







root.mainloop()