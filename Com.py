# This is a copy of MindPy made by me: at https://github.com/BostonA/MindPi/blob/master/Pi-Python/Com.py
import time, RPi.GPIO as GPIO
def toBinary(n):
    return ''.join(str(1 & int(n) >> i) for i in range(64)[::-1])
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
LEDon = False
# Python Codes
# The Init() must be ran first to Allert Mindstorms
# Frequency = Change this to calabrate (in Seconds)
f = 1
#
def On():
    print "LED on"
    GPIO.output(4, GPIO.HIGH)
def Off():
    print "LED off"
    GPIO.output(4, GPIO.LOW)
def Init():
    On()
    time.sleep(f)
    Off()
    time.sleep(f)
def Binary(Data):
    Off()

    LEDon = False
    for Digit in Data:
        if Digit == "1":
            if not LEDon:
                LEDon = True
                On()
        if Digit == "0":
            if LEDon:
                LEDon = False
                Off()
        time.sleep(f)
    Off()
def Numeral(Data, ma):
    Init()
    zeros = True
    binary = []
    num = 0
    b = toBinary(Data)
    for char in b:
        num = num+1
        if char != "0":
            zeros = False
        if zeros == False:
            binary.append(char)
    if ma >= 64:
        lenmax = 7
    elif ma >= 32:
        lenmax = 6
    elif ma >= 16:
        lenmax = 5
    elif ma >= 8:
        lenmax = 4
    elif ma >= 4:
        lenmax = 3
    elif ma >= 2:
        lenmax = 2
    elif ma >= 1:
        lenmax = 1
    while True:
        if lenmax == len(binary):
            break
        else:
            binary = ["0"] + binary
    print binary
    Binary(binary)


"""
def Hexadecimal(Data):
    print "Hex"
def ASCII(Data):
    print "ASCII"
"""
Numeral(3, 10)