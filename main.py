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

# btn starts false
prev_state = btn.value

while True:
    
    # if button is true
    while btn.value:
        if lcd.message != "button pressed":
            lcd.message = "button pressed"
        led.color = (0, 255, 0)
        
        
    # default state
    if lcd.message != "button unpressed":
        lcd.message = "button unpressed"
    
    led.color = (255, 0, 0)
    lcd.clear()
    prev_state = cur_state
    
    