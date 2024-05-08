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

red = board.D16
green = board.D20
blue = board.D21

led = adafruit_rgbled.RGBLED(red, blue, green)


btn = digitalio.DigitalInOut(board.D14)
btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.UP

prev_state = btn.value

while True:
    cur_state = btn.value
    if cur_state != prev_state:
        if not cur_state:
            lcd.clear
            lcd.message = "button down"
            led.color = (0, 255, 0)
        else:
            lcd.clear
            lcd.message = "button up"
            led.color = (255, 0, 0)
    prev_state = cur_state