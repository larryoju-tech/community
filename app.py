
import RPi.GPIO as GPIO # import Raspberry Pi GPIO library
import time

GPIO.setwarnings(False)# Ignore warning for now
GPIO.setmode(GPIO.BOARD) #Use physical pin numbering
# Set General Purpose Input Output(GPIO) Pin 4 (position 7) to be an input pin and set initial value to be pulled low(off)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

button_pressed = False

while True: # Run forever
    time.sleep(0.1)

    if GPIO.input(7) == GPIO.HIGH and not button_pressed:
        print("Someone has pressed the alert button!")
        button_pressed = True

    elif GPIO.input(7) == GPIO.LOW and button_pressed:
        button_pressed = False
