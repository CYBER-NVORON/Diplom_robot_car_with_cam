import RPi.GPIO as GPIO
import time

class Servo(object):

    def __init__(self, s1=22, s2=27, angle = 90):
        self.S1 = s1
        self.S2 = s2
        self.angle1 = angle
        self.angle2 = angle
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.S1,GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.S2,GPIO.OUT, initial=GPIO.LOW)
        self.SERVO1 = GPIO.PWM(self.S1, 50)
        self.SERVO2 = GPIO.PWM(self.S2, 50)
        self.SERVO1.start(7.5)
        self.SERVO2.start(7.5)
        time.sleep(1)
        self.SERVO1.stop()
        self.SERVO2.stop()

    
    def ServoAngle1(self, angle):
        pass
    
    def ServoAngle2(self, angle):
        pass
