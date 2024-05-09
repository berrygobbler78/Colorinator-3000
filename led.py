# import time
# import board
# import digitalio
# import adafruit_rgbled
# import adafruit_character_lcd.character_lcd as characterlcd

# lcd_rs = digitalio.DigitalInOut(board.D2)
# lcd_en = digitalio.DigitalInOut(board.D3)
# lcd_d7 = digitalio.DigitalInOut(board.D26)
# lcd_d6 = digitalio.DigitalInOut(board.D19)
# lcd_d5 = digitalio.DigitalInOut(board.D13)
# lcd_d4 = digitalio.DigitalInOut(board.D6)

# lcd_columns = 16
# lcd_rows = 2

# lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

# red_pin = board.D16
# green_pin = board.D20
# blue_pin = board.D21


# led = adafruit_rgbled.RGBLED(red_pin, blue_pin, green_pin)
# while True:
#     led.color = (187, 0, 255)

import time
import RPi.GPIO as GPIO

red = 16
green = 21
blue = 20

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

# Set up colors using PWM so we can control individual brightness.
RED = GPIO.PWM(red, 100)
GREEN = GPIO.PWM(green, 100)
BLUE = GPIO.PWM(blue, 100)
RED.start(0)
GREEN.start(0)
BLUE.start(0)

# Set a color by giving R, G, and B values of 0-255.
def setColor(rgb = []):
    # Convert 0-255 range to 0-100.
    rgb = [(x / 255.0) * 100 for x in rgb]
    RED.ChangeDutyCycle(rgb[0])
    GREEN.ChangeDutyCycle(rgb[1])
    BLUE.ChangeDutyCycle(rgb[2])

setColor([0, 255, 0])