
import RPi.GPIO as GPIO 
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

button_pressed = False

while True:
    time.sleep(0.1)

    if GPIO.input(7) == GPIO.HIGH and not button_pressed:
        print("Someone has pressed the alert button!")
        button_pressed = True

    elif GPIO.input(7) == GPIO.LOW and button_pressed:
        button_pressed = False
