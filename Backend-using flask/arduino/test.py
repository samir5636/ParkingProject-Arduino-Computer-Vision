import serial
import time
import cv2
import pytesseract

SerialObj = serial.Serial('/dev/ttyACM0') 
                  # ttyUSBx format on Linux
SerialObj.baudrate = 9600  # set Baud rate to 9600
SerialObj.bytesize = 8   # Number of data bits = 8
SerialObj.parity  ='N'   # No parity
SerialObj.stopbits = 1   # Number of Stop bits = 1
time.sleep(3)
SerialObj.write("Open door before user enter from the parking".encode())
SerialObj.close()      # Close the port
cap = cv2.VideoCapture(0)
while True:
    
    # data = SerialObj.readline().decode('utf-8').strip()
    ret, frame = cap.read()
    cv2.imshow('Camera Test', frame)
    # Perform text extraction on the captured image
    matricule = pytesseract.image_to_string(frame)
    print(f"matricule : {matricule}")
