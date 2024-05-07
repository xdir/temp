#import RPi.GPIO as GPIO


class Relay:
    pin = -1
    state = False;

    def __init__(self, pin):
        self.pin = pin
        #GPIO.setmode(GPIO.BCM)
        #GPIO.setup(self.pin, GPIO.OUT)  # pin = 17 ?

    def on(self):
        print("Turning on relay on pin: " + str(self.pin))
        self.state = True;
        #GPIO.output(self.pin, GPIO.HIGH)  # Turn relay on

    def off(self):
        print("Turning off relay on pin: " + str(self.pin))
        self.state = False;
        #GPIO.output(self.pin, GPIO.LOW)  # Turn relay off

    def is_on(self):
        #state = GPIO.input(self.pin)
        #return True if state == GPIO.HIGH else False
        return False
