import RPi.GPIO as GPIO
import time

class Servo(object):
	
	def __init__(self, s1=27, s2=22):
        self.ANGEL=90
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(s1,GPIO.OUT)
		GPIO.setup(s2,GPIO.OUT)
		self.SERVO1 = GPIO.PWM(s1,50)
		self.SERVO2 = GPIO.PWM(s2,50)
		self.SERVO1.start(5)
        self.SERVO2.start(5)
    
    def setAngleServo1(self):
        duty = float(self.ANGEL)/10.0 + 2.5
        self.SERVO1.ChangeDutyCycle(duty)
        time.sleep(1)
    
    def setAngleServo2(self, angle):
        duty = float(self.ANGEL)/10.0 + 2.5
        self.SERVO2.ChangeDutyCycle(duty)
        time.sleep(1)