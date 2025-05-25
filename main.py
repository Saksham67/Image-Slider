import tkinter as tk
from PIL import Image, ImageTk
import os
import random

# Configuration
image_folder = "images" 
delay = 500  

# Loads image paths
image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder)
               if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

# Tkinter window setup
root = tk.Tk()
root.title("Random Image Slider")

# Label to hold images
label = tk.Label(root)
label.pack()

def update_image():
    img_path = random.choice(image_files)
    img = Image.open(img_path)
    img = img.resize((600, 400))  
    photo = ImageTk.PhotoImage(img)
    label.config(image=photo)
    label.image = photo
    root.after(delay, update_image)

# Start the slider
update_image()
root.mainloop()
