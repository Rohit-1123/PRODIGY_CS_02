# Image Encryption and Decryption Tool (GUI)

A drag-and-drop GUI-based application to encrypt and decrypt image files using a numeric key. This tool shifts RGB values of image pixels for simple image obfuscation.

---

##  Features

- Encrypt and decrypt `.png`, `.jpg`, and `.jpeg` images.
- Drag-and-drop interface using `tkinterDnD2`.
- Key-based RGB pixel shifting algorithm.
- Option to save encrypted/decrypted image.
- Built with Python `Tkinter`, `Pillow (PIL)`, and `tkinterDnD2`.

---

## Tech Stack

- Python 3.x
- Tkinter
- tkinterDnD2
- Pillow (PIL)

---


## How It Works

Each pixel in the image is accessed and its RGB values are shifted:

```python
r = (r + key) % 256
g = (g + key) % 256
b = (b + key) % 256
```

For decryption, the shift is reversed:

```python
r = (r - key) % 256
g = (g - key) % 256
b = (b - key) % 256
```


Example usage:
To encrypt:

- Select image: secret_image.png
- Enter key: 10
- Click: Encrypt
- Saved as: encrypted_output.png

To decrypt:

- Select image: encrypted_output.png
- Enter key: 10
- Click: Decrypt
- Saved as: decrypted_output.png

