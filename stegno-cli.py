#!/usr/bin/env python3 

import cv2
import string

img = cv2.imread(input("Enter The Image: "))

secret_msg = input("Enter The Message: ")
password = input("Enter The Password: ")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

for i in range(len(secret_msg)):
    img[n, m, z] = d[secret_msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

save_path = input("Save File As: ")

cv2.imwrite(save_path , img)

#-----------------------------

message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption: ")
if password == pas:
    for i in range(len(secret_msg)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message: ", message)
else:
    print("Incorrect Password.")
