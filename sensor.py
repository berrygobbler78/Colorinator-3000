import RPi.GPIO as GPIO
import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

GPIO.cleanup()

s2 = 12
s3 = 25
signal = 24
NUM_CYCLES = 10

redPin = 16
greenPin = 20
bluePin = 21
#set pins as outputs

GPIO.cleanup()
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(s2,GPIO.OUT)
GPIO.setup(s3,GPIO.OUT)

GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)

GPIO.output(redPin, 0)
GPIO.output(greenPin, 0)
GPIO.output(bluePin, 0)

RED = GPIO.PWM(redPin, 100)
GREEN = GPIO.PWM(greenPin, 100)
BLUE = GPIO.PWM(bluePin, 100)
RED.start(0)
GREEN.start(0)
BLUE.start(0)

print("\n")
  

def setColor(rgb = []):
    # Convert 0-255 range to 0-100.
    rgb = [(x / 255.0) * 100 for x in rgb]
    RED.ChangeDutyCycle(rgb[0])
    GREEN.ChangeDutyCycle(rgb[1])
    BLUE.ChangeDutyCycle(rgb[2])


def loop():
  temp = 1
  while(1):  

    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.LOW)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start      #seconds to run for loop
    red  = NUM_CYCLES / duration   #in Hz
    print("red value - ",red)

    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    blue = NUM_CYCLES / duration
    print("blue value - ",blue)

    GPIO.output(s2,GPIO.HIGH)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    green = NUM_CYCLES / duration
    print("green value - ",green)
    time.sleep(2)  

    setColor([int(red), int(green), int(blue)])



def endprogram():
    GPIO.cleanup()

if __name__=='__main__':

    try:
        loop()

    except KeyboardInterrupt:
        endprogram()
    finally:
        GPIO.cleanup()