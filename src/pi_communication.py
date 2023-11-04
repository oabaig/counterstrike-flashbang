import socket
from time import sleep
import RPi.GPIO as GPIO
from dotenv import load_dotenv
import os


host = ""
port = int(os.getenv('PORT'))

flashDuration = 0.2  # seconds
flashing = False

GPIO_PIN = 16


def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("Socket bind comlete.")
    return s


def setupConnection():
    s.listen(1)  # Allows one connection at a time.
    conn, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    return conn


def FLASH():
    GPIO.output(GPIO_PIN, True)

    sleep(flashDuration)

    GPIO.output(GPIO_PIN, False)

    return


def dataTransfer(conn):
    # A big loop that sends/receives data until told not to.
    while True:
        # Receive the data
        data = conn.recv(1024)  # receive the data
        data = data.decode("utf-8")
        # Split the data such that you separate the command
        # from the rest of the data.
        dataMessage = data.split(" ", 1)
        command = dataMessage[0]
        if command:
            print(command)

        if command == "FLASH":
            reply = "FLASHING!!!"
            FLASH()
        else:
            reply = "Unknown Command"
        # Send the reply back to the client
        conn.sendall(str.encode(reply))
        print("Data has been sent!")


GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)
GPIO.output(GPIO_PIN, False)

s = setupServer()

while True:
    try:
        conn = setupConnection()
        dataTransfer(conn)
    except:
        break
