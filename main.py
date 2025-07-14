import serial
import time

correct_password = "1234"

ser = serial.Serial('COM3', 9600, timeout=1)  # Replace 'COM3' with your microcontroller port
time.sleep(2)

password = input("Enter Password: ")

if password == correct_password:
    print("Password Accepted. Turning ON circuit.")
    ser.write(b'1')
else:
    print("Incorrect Password. Access Denied.")
    ser.write(b'0')

ser.close()
