import RPi.GPIO as GPIO

from time import sleep
import time
import lcd
import translate

GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(8,GPIO.OUT,initial = GPIO.LOW)

# while True: # Run forever
#     GPIO.output(8, GPIO.HIGH) # Turn on
#     sleep(1)                  # Sleep for 1 second
#     GPIO.output(8, GPIO.LOW)  # Turn off
#     sleep(1)                  # Sleep for 1 second
class MorseEncoder:
    btn = 7
    counter = 0
    msg = ""
    dot_threshold = 0.5
    dash threshold = 2
    
    def __init__(self):

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(MorseEncoder.btn,GPIO.IN)
        GPIO.add_event_detect(MorseEncoder.btn,GPIO.BOTH,callback=self.click,bouncetime=20)
        self.counter = 0
        self.message = ""
        self.btn_start = 0
        self.btn_end = 0
        self.lcd = lcd.LCD() 

        self.run()

    
    def add_click_to_msg(self,elapsed){
        if GPIO.input(self.btn)==0:
            if 1<elapsed<3:
                self.send_message()
            elif elapsed<5:
                self.send_message()
                self.message=" "
                sef.send_message()
            
        else:
            if elapsed<0.5:
                self.message+="."
            else:
                self.message+="_"
        print(self.message)
            
            
        




    }

        
    
    def click(self,channel):
        if GPIO.input(self.btn)==0:
            self.btn_start = time.time()
            elapsed = self.btn_start - self.btn_end
            self.add_click_to_msg(elapsed)
        else:
            slef.btn_end = time.time()
            elapsed = self.btn_end-self.btn_start
            self.add_click_to_msg(elapsed)
            
    
    def send_message(self):
        
        message = translate.morseToEng(self.msg)
        self.lcd.add_to_msg(message)
        print(message)
        self.msg = ""
        
    def run(self):
        while True:
            pass
    

        
        
e = MorseEncoder()      
 
