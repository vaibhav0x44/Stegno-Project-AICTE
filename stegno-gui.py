#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import subprocess

# Function to open file
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
    if file_path:
        text_box.config(state="normal")
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, file_path)
        text_box.config(state="disabled")
        file_path_var.set(file_path)


def encode_message(image_path, secret_msg, password):
    try:
        img = cv2.imread(image_path)
  
        d = {chr(i): i for i in range(255)}

        
        m, n, z = 0, 0, 0
        for char in secret_msg:
            img[n, m, z] = d[char]
            n += 1
            m += 1
            z = (z + 1) % 3

        return img

    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None


def encode_and_save():
    image_path = file_path_var.get()
    secret_msg = message_input.get()
    password = password_input.get()

    if not image_path:
        messagebox.showwarning("WARNING", "Please select an image")
        return

    if not secret_msg:
        messagebox.showwarning("WARNING", "Please enter a message")
        return

    if not password:
        messagebox.showwarning("WARNING", "Please enter a password")
        return

    encoded_image = encode_message(image_path, secret_msg, password)
    if encoded_image is not None:
        save_path = filedialog.asksaveasfilename(filetypes=[("All Files","*.*")])
        if save_path:
            cv2.imwrite(save_path, encoded_image)
            messagebox.showinfo("Success", "Encoded image saved successfully")


def decode_message():
    subprocess.run(["python3", "decode_script.py"])

# GUI Setup
window = tk.Tk()
window.geometry("500x350")
window.title("SteganoGraphy GUI Tool")

# Label
label = tk.Label(window, text="Stegn0-XD v1.0", fg="red", font=("DejaVu Sans", 16, "bold"), relief="ridge", bd=3)
label.grid(padx=175, pady=10, columnspan=2)

# File Selection
text_box = tk.Text(window, height=1, width=40)
text_box.grid(row=1, column=1, pady=10)
text_box.config(state='disabled')

open_button = tk.Button(window, text="Image File", command=open_file)
open_button.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Message Input
message_label = tk.Label(window, text="Message", font=("Helvetica", 14))
message_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")

message_input = tk.Entry(window, font=("Helvetica", 12), width=25)
message_input.grid(row=2, pady=10, column=1)

# Password Input
password_label = tk.Label(window, text="Password", font=("Helvetica", 14))
password_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")

password_input = tk.Entry(window, show="*", font=(50), width=35)
password_input.grid(row=3, pady=10, column=1)

# Encode Button
tk.Button(window, text="ENCODE", font=("Helvetica", 14, "bold"), command=encode_and_save, width=15).grid(row=4, columnspan=2, padx=20, pady=10)

# Decode Button
tk.Button(window, text="DECODE", font=("Helvetica", 14, "bold"), command=decode_message, width=15).grid(row=5, columnspan=2, padx=20, pady=10)

# File Path Variable
file_path_var = tk.StringVar()

window.mainloop()
