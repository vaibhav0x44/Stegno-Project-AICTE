#!/usr/bin/env python3

import cv2
import string

# Decryption Dictionary
c = {i: chr(i) for i in range(255)}


image_path = input("Image File Name: ")
password_attempt = input("Enter passcode: ")

# Load image
img = cv2.imread(image_path)
if img is None:
    print("Error: Invalid image file!")
    exit(1)

pas = input("Re-enter Passcode: ")

if password_attempt == pas:
    message = ""  
    n, m, z = 0, 0, 0  

    for _ in range(1000):  
        try:
            message += c[img[n, m, z]]
            n += 1
            m += 1
            z = (z + 1) % 3
        except IndexError:
            break 

    print("Decryption message:", message)
else:
    print("Incorrect Password.")
