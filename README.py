import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)
GPIO.output(5, GPIO.HIGH)
GPIO.output(5, GPIO.LOW)
try:
    while 1:
        GPIO.output(5, GPIO.HIGH)
        time.sleep(0.25)
        GPIO.output(5, GPIO.LOW)
        time.sleep(0.25)
except KeyboardInterrupt:
     GPIO.cleanup()
