import RPi.GPIO as GPIO

from time import sleep
import time
from lcd import LCD
import translate
import threading
from translate import morse_to_eng, eng_to_morse
GPIO.setwarnings(False)

 

# while True: # Run forever
#     GPIO.output(8, GPIO.LOW) # Turn on
#     sleep(1)                  # Sleep for 1 second
#     GPIO.output(8, GPIO.LOW)  # Turn off
#     sleep(1)                  # Sleep for 1 second
class MorseEncoder:
    btn = 4
    led = 14
    counter = 0
    msg = ""
    dot_threshold = 0.5

    MSG = "lolxd"
    DOT = 0.5
    DASH = 1.5
    SIGNAL_DELAY = 0.5
    CHAR_DELAY = 1.5
    WORD_DELAY = 3.5
    SPACE = "   "

    BUZZER_PORT = 17

    def __init__(self):

        GPIO.setup(MorseEncoder.btn,GPIO.IN)
        GPIO.setup(8,GPIO.OUT,initial = GPIO.LOW)
        GPIO.setup(self.BUZZER_PORT, GPIO.OUT, initial = GPIO.LOW)
        GPIO.add_event_detect(MorseEncoder.btn,GPIO.BOTH,callback=self.click,bouncetime=20)
        self.counter = 0

        self.btn_start = 0
        self.btn_end = 0
        self.lcd = LCD() 

        self.run()
    
    def add_click_to_msg(self,elapsed,buttonDown):
        if buttonDown:
            if 1.5<elapsed<3.5:
                self.send_message()
            elif 3.5<=elapsed:
                self.send_message()
                self.msg=" "
                self.send_message()
            
        else:
            if elapsed<self.dot_threshold:
                self.msg+="."
            else:
                self.msg+="-"
    
    def click(self,channel):
        if GPIO.input(self.btn)==0:
            self.btn_start = time.time()
            elapsed = self.btn_start - self.btn_end
            self.add_click_to_msg(elapsed,True)
        else:
            self.btn_end = time.time()
            elapsed = self.btn_end-self.btn_start
            self.add_click_to_msg(elapsed,False)
    
    def send_message(self):
        message = morse_to_eng[self.msg]
        self.lcd.add_to_msg(message)
        self.msg = ""

    def morse_to_buzzer(self): 
        morse = [eng_to_morse[c] for c in self.MSG]
        prev = ''

        for c in morse:
            if c == self.SPACE:
                if prev == c:
                    sleep(self.WORD_DELAY)
                else:
                    sleep(self.WORD_DELAY - self.CHAR_DELAY)
            else:
                for s in c:
                    if s == '.':
                        GPIO.output(self.BUZZER_PORT, GPIO.HIGH)
                        sleep(self.DOT)
                        GPIO.output(self.BUZZER_PORT, GPIO.LOW)
                    elif s == '-':
                        GPIO.output(self.BUZZER_PORT, GPIO.HIGH)
                        sleep(self.DASH)
                
                        GPIO.output(self.BUZZER_PORT, GPIO.LOW)
                    sleep(self.SIGNAL_DELAY)

                sleep(self.CHAR_DELAY - self.SIGNAL_DELAY)

            prev = c

	msg = ''

    def run(self):
        while True:
            self.morse_to_buzzer()

e = MorseEncoder()      
 
