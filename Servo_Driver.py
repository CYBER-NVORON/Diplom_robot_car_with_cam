import RPi.GPIO as GPIO

class Servo(object):

    def __init__(self, s1=27, s2=22, angle = 90):
        self.S1 = s1
        self.S2 = s2
        self.angle1 = angle
        self.angle2 = angle
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(s1,GPIO.OUT)
        GPIO.setup(s2,GPIO.OUT)
        self.stop()
        self.SERVO1 = GPIO.PWM(s1,50)
        self.SERVO2 = GPIO.PWM(s2,50)
        self.SERVO1.start(5)
        self.SERVO2.start(5)

    def stop(self):
        GPIO.output(self.S1,GPIO.LOW)
        GPIO.output(self.S2,GPIO.LOW)

    def setAngleServo1(self, angle):
        self.angle1 += angle
        duty = float(self.angle1)/10.0 + 2.5
        self.SERVO1.ChangeDutyCycle(duty)
    
    def setAngleServo2(self, angle):
        self.angle2 += angle
        duty = float(self.angle2)/10.0 + 2.5
        self.SERVO2.ChangeDutyCycle(duty)