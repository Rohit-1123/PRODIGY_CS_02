import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image

selected_image_path = None

# Convert to RGB if needed
def ensure_rgb(image):
    if image.mode != "RGB":
        image = image.convert("RGB")
    return image

# Encrypt or decrypt image based on button click
def process_image(encrypt=True):
    global selected_image_path

    if not selected_image_path:
        messagebox.showerror("No Image", "Please drag and drop an image file first.")
        return

    try:
        key = int(key_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Key", "Please enter a valid number.")
        return

    try:
        image = ensure_rgb(Image.open(selected_image_path))
        pixels = image.load()
    except Exception as e:
        messagebox.showerror("Error", f"Unable to open image: {e}")
        return

    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            shift = key if encrypt else -key
            r = (r + shift) % 256
            g = (g + shift) % 256
            b = (b + shift) % 256
            pixels[i, j] = (r, g, b)

    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG Image", "*.png")])
    if save_path:
        image.save(save_path)
        msg = "Encrypted" if encrypt else "Decrypted"
        messagebox.showinfo("Done", f"{msg} image saved as:\n{save_path}")

# Handle file drop
def drop(event):
    global selected_image_path
    selected_image_path = event.data.strip("{}")  # Handles paths with spaces
    image_label.config(text=f"Selected: {selected_image_path}")

#GUI Setup 
root = TkinterDnD.Tk()
root.title("Image Encryptor / Decryptor (with Drag & Drop)")
root.geometry("450x300")
root.resizable(False, False)

tk.Label(root, text="Drag & Drop an Image Below:", font=("Arial", 12)).pack(pady=10)

# Drag & Drop label
image_label = tk.Label(root, text="Drop your image here", relief="solid", height=3, font=("Arial", 10), bg="#f0f0f0")
image_label.pack(pady=5, fill="x", padx=20)
image_label.drop_target_register(DND_FILES)
image_label.dnd_bind('<<Drop>>', drop)

# Key input
tk.Label(root, text="Enter Key (number):", font=("Arial", 12)).pack(pady=10)
key_entry = tk.Entry(root, font=("Arial", 12))
key_entry.pack(pady=5)

# Encrypt/Decrypt buttons
tk.Button(root, text="Encrypt", font=("Arial", 12), bg="lightgreen",
          command=lambda: process_image(encrypt=True)).pack(pady=8)

tk.Button(root, text="Decrypt", font=("Arial", 12), bg="lightblue",
          command=lambda: process_image(encrypt=False)).pack(pady=5)

root.mainloop()
