import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to encrypt the message in the image
def encrypt_image():
    img_path = img_path_entry.get()
    msg = msg_entry.get()
    password = password_entry.get()

    if not img_path or not msg or not password:
        messagebox.showerror("Error", "Please fill all fields!")
        return

    img = cv2.imread(img_path)
    if img is None:
        messagebox.showerror("Error", "Invalid image path!")
        return

    # Store the message length in the first pixel
    msg_length = len(msg)
    img[0, 0, 0] = msg_length  # Store length in the first pixel (R channel)

    # Encrypt the message
    d = {chr(i): i for i in range(255)}
    m, n, z = 0, 1, 0  # Start from the second pixel to avoid overwriting the length

    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n += 1
        m += 1
        z = (z + 1) % 3

    encrypted_path = "encryptedImage.png"
    cv2.imwrite(encrypted_path, img, [cv2.IMWRITE_PNG_COMPRESSION, 0])  # Save without compression
    messagebox.showinfo("Success", f"Image encrypted and saved as {encrypted_path}")
    os.system(f"start {encrypted_path}")  # Open the image on Windows

# Function to decrypt the message from the image
def decrypt_image():
    encrypted_path = encrypted_path_entry.get()
    password = decrypt_password_entry.get()

    if not encrypted_path or not password:
        messagebox.showerror("Error", "Please fill all fields!")
        return

    img = cv2.imread(encrypted_path, cv2.IMREAD_UNCHANGED)  # Load image without modification
    if img is None:
        messagebox.showerror("Error", "Invalid image path!")
        return

    # Retrieve the message length from the first pixel
    msg_length = img[0, 0, 0]

    # Decrypt the message
    c = {i: chr(i) for i in range(255)}
    m, n, z = 0, 1, 0  # Start from the second pixel
    message = ""

    if password == password_entry.get():
        for _ in range(msg_length):  # Use the stored message length
            message += c[img[n, m, z]]
            n += 1
            m += 1
            z = (z + 1) % 3
        messagebox.showinfo("Decrypted Message", f"Decrypted message: {message}")
    else:
        messagebox.showerror("Error", "Incorrect password!")

# Function to open file dialog for image selection
def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    img_path_entry.delete(0, tk.END)
    img_path_entry.insert(0, file_path)

# Function to open file dialog for encrypted image selection
def browse_encrypted_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
    encrypted_path_entry.delete(0, tk.END)
    encrypted_path_entry.insert(0, file_path)

# Function to create a gradient background
def create_gradient_background(canvas, width, height):
    colors = ["#ffffff", "#f3f6f4", "#eeeeee", "#bcbcbc"]  # Multicolor gradient
    for i in range(len(colors)):
        canvas.create_rectangle(
            0, i * (height / len(colors)), width, (i + 1) * (height / len(colors)),
            fill=colors[i], outline=""
        )

# Function to add hover effect to buttons
def on_enter(e, button, hover_color):
    button.config(bg=hover_color)

def on_leave(e, button, original_color):
    button.config(bg=original_color)

# Create the main window
root = tk.Tk()
root.title("Image Steganography")
root.geometry("500x400")

# Create a Canvas for the multicolor background
canvas = tk.Canvas(root, width=500, height=400)
canvas.pack(fill="both", expand=True)

# Draw the gradient background
create_gradient_background(canvas, 500, 400)

# Custom Fonts
title_font = ("Helvetica", 16, "bold")
label_font = ("Helvetica", 12)
entry_font = ("Helvetica", 11)
button_font = ("Helvetica", 12, "bold")

# Custom Colors
entry_bg = "#4C566A"
button_bg = "#5E81AC"
button_fg = "#ECEFF4"
hover_color = "#88C0D0"  # Hover color for buttons

# Create and place widgets on the canvas
tk.Label(canvas, text="Image Steganography", font=title_font, bg="white", fg="black").place(relx=0.5, rely=0.1, anchor="center")

tk.Label(canvas, text="Image Path:", font=label_font, bg="white", fg="black").place(relx=0.1, rely=0.2, anchor="w")
img_path_entry = tk.Entry(canvas, width=40, font=entry_font, bg=entry_bg, fg="white", insertbackground="white")
img_path_entry.place(relx=0.1, rely=0.25, anchor="w")
browse_button = tk.Button(canvas, text="Browse", command=browse_image, font=button_font, bg=button_bg, fg=button_fg, relief="flat")
browse_button.place(relx=0.8, rely=0.25, anchor="center")
browse_button.bind("<Enter>", lambda e: on_enter(e, browse_button, hover_color))
browse_button.bind("<Leave>", lambda e: on_leave(e, browse_button, button_bg))

tk.Label(canvas, text="Secret Message:", font=label_font, bg="white", fg="black").place(relx=0.1, rely=0.35, anchor="w")
msg_entry = tk.Entry(canvas, width=40, font=entry_font, bg=entry_bg, fg="white", insertbackground="white")
msg_entry.place(relx=0.1, rely=0.4, anchor="w")

tk.Label(canvas, text="Password:", font=label_font, bg="white", fg="black").place(relx=0.1, rely=0.5, anchor="w")
password_entry = tk.Entry(canvas, width=40, font=entry_font, bg=entry_bg, fg="white", insertbackground="white", show="*")
password_entry.place(relx=0.1, rely=0.55, anchor="w")

encrypt_button = tk.Button(canvas, text="Encrypt", command=encrypt_image, font=button_font, bg=button_bg, fg=button_fg, relief="flat")
encrypt_button.place(relx=0.5, rely=0.65, anchor="center")
encrypt_button.bind("<Enter>", lambda e: on_enter(e, encrypt_button, hover_color))
encrypt_button.bind("<Leave>", lambda e: on_leave(e, encrypt_button, button_bg))

tk.Label(canvas, text="Encrypted Image Path:", font=label_font, bg="white", fg="black").place(relx=0.1, rely=0.75, anchor="w")
encrypted_path_entry = tk.Entry(canvas, width=40, font=entry_font, bg=entry_bg, fg="white", insertbackground="white")
encrypted_path_entry.place(relx=0.1, rely=0.8, anchor="w")
browse_encrypted_button = tk.Button(canvas, text="Browse", command=browse_encrypted_image, font=button_font, bg=button_bg, fg=button_fg, relief="flat")
browse_encrypted_button.place(relx=0.8, rely=0.8, anchor="center")
browse_encrypted_button.bind("<Enter>", lambda e: on_enter(e, browse_encrypted_button, hover_color))
browse_encrypted_button.bind("<Leave>", lambda e: on_leave(e, browse_encrypted_button, button_bg))

tk.Label(canvas, text="Decryption Password:", font=label_font, bg="white", fg="black").place(relx=0.1, rely=0.9, anchor="w")
decrypt_password_entry = tk.Entry(canvas, width=40, font=entry_font, bg=entry_bg, fg="white", insertbackground="white", show="*")
decrypt_password_entry.place(relx=0.1, rely=0.95, anchor="w")

decrypt_button = tk.Button(canvas, text="Decrypt", command=decrypt_image, font=button_font, bg=button_bg, fg=button_fg, relief="flat")
decrypt_button.place(relx=0.5, rely=0.95, anchor="center")
decrypt_button.bind("<Enter>", lambda e: on_enter(e, decrypt_button, hover_color))
decrypt_button.bind("<Leave>", lambda e: on_leave(e, decrypt_button, button_bg))

# Run the main loop
root.mainloop()
