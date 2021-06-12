import RPi.GPIO as GPIO

from time import sleep
import time
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
    message = ""
    
    def __init__(self):

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(MorseEncoder.btn,GPIO.IN)
        GPIO.add_event_detect(MorseEncoder.btn,GPIO.BOTH,callback=self.click,bouncetime=20)
        self.counter = 0
        self.message = ""
        self.btn_start = 0

        self.run()

        
        
    
    def click(self,channel):
        if GPIO.input(self.btn)==0:
            self.btn_start = time.time()
        else:
            end = time.time()
            elapsed = end-self.btn_start
            print(elapsed)
    
    def send_message(self):
        pass
    def run(self):
        while True:
            pass
    

        
        
e = MorseEncoder()      
 
