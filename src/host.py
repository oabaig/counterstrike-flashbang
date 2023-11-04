import numpy as np
from PIL import ImageGrab
import cv2
import os
from dotenv import load_dotenv
import socket

HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))

def is_white(img):
    return np.mean(img) > 200

def main():

    flash = False

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:
        video = ImageGrab.grab()

        if is_white(video):
            if not flash:
                flash = True
                s.send('FLASH'.encode('utf-8'))
        elif flash:
            s.send('STOP'.encode('utf-8'))
            flash = False
main()
