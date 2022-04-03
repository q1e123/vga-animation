import sys

import cv2

def getMSB(number):
    binary = bin(number)
    bitList = list(binary)
    if len(bitList) <= 8:
        padding = [0 for _ in range(8 - len(bitList))]
        padding.extend(bitList)
        bitList = padding
    bitList.remove('b')
    bitList = bitList[1:]
    msb = bitList[0]
    return msb

print(getMSB(4),getMSB(8), getMSB(4), getMSB(128),getMSB(255))

image_path = sys.argv[1]

image = cv2.imread(image_path)
rows,cols,_ = image.shape

states = []

for i in range(rows):
    row = []
    for j in range(cols):
        pixel = image[i,j]
        r = pixel[0]
        g = pixel[1]
        b = pixel[2]

