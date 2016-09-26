import RPi.GPIO as GPIO
import picamera
from django.conf import settings

GPIO.setmode(GPIO.BCM)
for pin in settings.PINS:
    GPIO.setup(pin, GPIO.OUT)

pwm_a = GPIO.PWM(settings.EN_A, 500)
pwm_b = GPIO.PWM(settings.EN_B, 500)


def forward(rate=100):
    pwm_a.start(0)
    pwm_b.start(0)

    GPIO.output(settings.IN_1, False)
    GPIO.output(settings.IN_2, True)

    GPIO.output(settings.IN_3, False)
    GPIO.output(settings.IN_4, True)

    pwm_a.start(rate)
    pwm_b.start(rate)


def reverse(rate=100):
    pwm_a.start(0)
    pwm_b.start(0)

    GPIO.output(settings.IN_1, True)
    GPIO.output(settings.IN_2, False)

    GPIO.output(settings.IN_3, True)
    GPIO.output(settings.IN_4, False)

    pwm_a.start(rate)
    pwm_b.start(rate)


def stop(rate=100):
    pwm_a.start(0)
    pwm_b.start(0)

    GPIO.output(settings.IN_1, False)
    GPIO.output(settings.IN_2, False)

    GPIO.output(settings.IN_3, False)
    GPIO.output(settings.IN_4, False)

    pwm_a.start(rate)
    pwm_b.start(rate)


def left(rate=100):
    pwm_a.start(0)
    pwm_b.start(0)

    GPIO.output(settings.IN_1, False)
    GPIO.output(settings.IN_2, True)

    GPIO.output(settings.IN_3, True)
    GPIO.output(settings.IN_4, False)

    pwm_a.start(rate)
    pwm_b.start(rate)


def right(rate=100):
    pwm_a.start(0)
    pwm_b.start(0)

    GPIO.output(settings.IN_1, True)
    GPIO.output(settings.IN_2, False)

    GPIO.output(settings.IN_3, False)
    GPIO.output(settings.IN_4, True)

    pwm_a.start(rate)
    pwm_b.start(rate)


def center():
    free()


def free():
    pwm_a.start(0)
    pwm_b.start(0)
    GPIO.output(settings.IN_1, False)
    GPIO.output(settings.IN_2, False)
    GPIO.output(settings.IN_3, False)
    GPIO.output(settings.IN_4, False)


def photo():
    with picamera.PiCamera() as camera:
        camera.capture('tmp.jpg')

