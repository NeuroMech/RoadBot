import RPi.GPIO as GPIO
from time import sleep

IN1=3
IN2=5
IN3=7
IN4=8
IN5=11
IN6=13
IN7=15
IN8=16
EN0=29

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(IN5, GPIO.OUT)
GPIO.setup(IN6, GPIO.OUT)
GPIO.setup(IN7, GPIO.OUT)
GPIO.setup(IN8, GPIO.OUT)
GPIO.setup(EN0, GPIO.OUT)
speed=GPIO.PWM(EN0,100)
speed.start(75)
while True:
    GPIO.output(IN1, GPIO.HIGH) # white back
    GPIO.output(IN2, GPIO.LOW)  
    GPIO.output(IN3, GPIO.LOW)  # while forward
    GPIO.output(IN4, GPIO.HIGH)
    PIO.output(IN5, GPIO.LOW)   # black forward
    GPIO.output(IN6, GPIO.HIGH)
    GPIO.output(IN7, GPIO.LOW)  # black back
    GPIO.output(IN8, GPIO.HIGH)
GPIO.cleanup()
