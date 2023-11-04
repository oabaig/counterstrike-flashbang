import numpy as np
from PIL import ImageGrab
import cv2
import os
from dotenv import load_dotenv

import socket

host = os.getenv('HOST')
port = int(os.getenv('PORT'))

def is_white(img):
    return np.mean(img) > 200

def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    while True:
        video = ImageGrab.grab()

        if is_white(video):
            s.send('FLASH'.encode('utf-8'))
            print("FLASH")

        cv2.imshow('window', np.array(video))

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()
