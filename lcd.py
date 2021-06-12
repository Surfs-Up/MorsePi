import board
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd
class LCD:
    def __init__(self):
        lcd_rs = digitalio.DigitalInOut(board.D26)
        lcd_en = digitalio.DigitalInOut(board.D19)
        lcd_d4 = digitalio.DigitalInOut(board.D13)
        lcd_d5 = digitalio.DigitalInOut(board.D6)
        lcd_d6 = digitalio.DigitalInOut(board.D5)
        lcd_d7 = digitalio.DigitalInOut(board.D11)
        lcd_backlight = digitalio.DigitalInOut(board.D15)
        self.lcd_columns = 16
        self.lcd_rows = 2
        self.lcd = character_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, self.lcd_columns, self.lcd_rows, lcd_backlight)
        self.message = ""
    def add_to_msg(self,l):
        self.message+=l
        self.lcd.message = self.message
        print(self.message)












