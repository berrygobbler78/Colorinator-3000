import time
import board
import digitalio
import adafruit_rgbled
import adafruit_character_lcd.character_lcd as characterlcd

# LED
red_pin = board.D16
green_pin = board.D20
blue_pin = board.D21

led = adafruit_rgbled.RGBLED(red_pin, blue_pin, green_pin)

# color sensor
s0 = digitalio.DigitalInOut(board.D12)
s1 = digitalio.DigitalInOut(board.D7)
s2 = digitalio.DigitalInOut(board.D8)
s3 = digitalio.DigitalInOut(board.D25)
out = digitalio.DigitalInOut(board.D24)

s0.direction = digitalio.Direction.OUTPUT
s1.direction = digitalio.Direction.OUTPUT
s2.direction = digitalio.Direction.OUTPUT
s3.direction = digitalio.Direction.OUTPUT

out.direction = digitalio.Direction.INPUT

while True:
    led.color = (187, 0, 255)