import sys
from turtle import st

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

def get_states(image_path):
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
            rgb = '{}{}{}'.format(getMSB(r), getMSB(g), getMSB(b))
            row.append(rgb)
        states.append(row)
    return states

def write_states_to_file(states,states_file_name):
    with open(states_file_name, 'w') as states_file:
        for row in states:
            for rgb in row:
                states_file.write(rgb + ' ')

image_path = sys.argv[1]
states_file_name = sys.argv[2]
print('Getting states...')
states = get_states(image_path)
print('Done getting states!')
print('Writing to output file...')
write_states_to_file(states, states_file_name)
print('Done!')
