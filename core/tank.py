import RPi.GPIO as GPIO
import picamera
from django.conf import settings

GPIO.setmode(GPIO.BCM)
for pin in settings.PINS:
    GPIO.setup(pin, GPIO.OUT)

pwm_a = GPIO.PWM(settings.EN_A, 500)
pwm_b = GPIO.PWM(settings.EN_B, 500)


def forward(rate=100):
    GPIO.output(settings.EN_A, False)
    GPIO.output(settings.EN_B, False)

    GPIO.output(settings.IN_1, False)
    GPIO.output(settings.IN_2, True)

    GPIO.output(settings.IN_3, False)
    GPIO.output(settings.IN_4, True)

    GPIO.output(settings.EN_A, True)
    GPIO.output(settings.EN_B, True)


def reverse(rate=100):
    GPIO.output(settings.EN_A, False)
    GPIO.output(settings.EN_B, False)

    GPIO.output(settings.IN_1, True)
    GPIO.output(settings.IN_2, False)

    GPIO.output(settings.IN_3, True)
    GPIO.output(settings.IN_4, False)

    GPIO.output(settings.EN_A, True)
    GPIO.output(settings.EN_B, True)


def stop(rate=100):
    GPIO.output(settings.EN_A, False)
    GPIO.output(settings.EN_B, False)

    GPIO.output(settings.IN_1, False)
    GPIO.output(settings.IN_2, False)

    GPIO.output(settings.IN_3, False)
    GPIO.output(settings.IN_4, False)

    GPIO.output(settings.EN_A, True)
    GPIO.output(settings.EN_B, True)


def left(rate=100):
    GPIO.output(settings.EN_A, False)
    GPIO.output(settings.EN_B, False)

    GPIO.output(settings.IN_1, True)
    GPIO.output(settings.IN_2, False)

    GPIO.output(settings.IN_3, False)
    GPIO.output(settings.IN_4, True)

    GPIO.output(settings.EN_A, True)
    GPIO.output(settings.EN_B, True)


def right(rate=100):
    GPIO.output(settings.EN_A, False)
    GPIO.output(settings.EN_B, False)

    GPIO.output(settings.IN_1, False)
    GPIO.output(settings.IN_2, True)

    GPIO.output(settings.IN_3, True)
    GPIO.output(settings.IN_4, False)

    GPIO.output(settings.EN_A, True)
    GPIO.output(settings.EN_B, True)


def center():
    forward()


def free():
    GPIO.output(settings.EN_A, False)
    GPIO.output(settings.EN_B, False)
    GPIO.output(settings.IN_1, False)
    GPIO.output(settings.IN_2, False)
    GPIO.output(settings.IN_3, False)
    GPIO.output(settings.IN_4, False)

def photo():
    with picamera.PiCamera() as camera:
        camera.capture('tmp.jpg')

