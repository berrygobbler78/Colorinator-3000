import time
import board
import digitalio
import adafruit_rgbled
import adafruit_character_lcd.character_lcd as characterlcd

lcd_rs = digitalio.DigitalInOut(board.D2)
lcd_en = digitalio.DigitalInOut(board.D3)
lcd_d7 = digitalio.DigitalInOut(board.D26)
lcd_d6 = digitalio.DigitalInOut(board.D19)
lcd_d5 = digitalio.DigitalInOut(board.D13)
lcd_d4 = digitalio.DigitalInOut(board.D6)

lcd_columns = 16
lcd_rows = 2

lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

red_pin = board.D16
green_pin = board.D20
blue_pin = board.D21

# while True:
#     lcd.message = "Hold button to select color"
#     cur_state = btn.value
#     if cur_state != prev_state:
#         if not cur_state:
#             lcd.message = "btn"
#         else:
#             lcd.message = "btn up"


led = adafruit_rgbled.RGBLED(red_pin, blue_pin, green_pin)
while True:
    led.color = (187, 0, 255)