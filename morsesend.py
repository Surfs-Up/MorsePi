import RPi.GPIO as GPIO

from time import sleep
import time
from lcd import LCD
import translate
import threading
from translate import morse_to_eng
GPIO.setwarnings(False)

# 

# while True: # Run forever
#     GPIO.output(8, GPIO.HIGH) # Turn on
#     sleep(1)                  # Sleep for 1 second
#     GPIO.output(8, GPIO.LOW)  # Turn off
#     sleep(1)                  # Sleep for 1 second
class MorseEncoder:
    btn = 4
    led = 14
    counter = 0
    msg = ""
    dot_threshold = 0.5

    
    def __init__(self):

        GPIO.setup(MorseEncoder.btn,GPIO.IN)
        GPIO.setup(8,GPIO.OUT,initial = GPIO.LOW)
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
        
    def run(self):
        while True:
            pass
    

        
        
e = MorseEncoder()      
 
