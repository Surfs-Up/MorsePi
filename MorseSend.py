import RPi.GPIO as GPIO

from time import sleep
GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(8,GPIO.OUT,initial = GPIO.LOW)

# while True: # Run forever
#     GPIO.output(8, GPIO.HIGH) # Turn on
#     sleep(1)                  # Sleep for 1 second
#     GPIO.output(8, GPIO.LOW)  # Turn off
#     sleep(1)                  # Sleep for 1 second
class MorseEncoder:
    clk = 11
    dt = 12
    btn = 10
    counter = 0
    clkLastState = 0
    message = ""
    def __init__(self):

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(MorseEncoder.clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(MorseEncoder.dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(MorseEncoder.btn,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(MorseEncoder.btn,GPIO.RISING,callback=self.click,bouncetime=20)
        self.counter = 0
        self.clkLastState = GPIO.input(MorseEncoder.clk)
        self.message = ""
        self.detect_rotary()
        
    
    def click(self,channel):

        print("click")
    def detect_rotary(self):
        try:
            while True:
                clkState = GPIO.input(MorseEncoder.clk)
                dtState = GPIO.input(MorseEncoder.dt)
                if clkState != self.clkLastState:
                    if dtState!=clkState:
                        self.counter+=1
                    else: self.counter-=1
                    print(self.counter)
                self.clkLastState = clkState
                sleep(0.01)
        finally:
            GPIO.cleanup()
    def send_message(self):
        pass

        
        
e = MorseEncoder()      
 
