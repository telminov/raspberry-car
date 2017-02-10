# import picamera
from django.conf import settings
from pyfirmata import Arduino, util


class Car:

    def __init__(self):
        self._board = None
        # пины тягового двигателя
        self._pull_direction_pin = settings.PIN_H1
        self._pull_force_pin = settings.PIN_E1
        # пины руля
        self._rudder_direction_pin = settings.PIN_H2
        self._rudder_force_pin = settings.PIN_E2

    def _get_board(self):
        if not self._board:
            self._board = Arduino(settings.ARDUINO_PATH)
        return self._board

    def forward(self):
        board = self._get_board()
        board.digital[self._pull_direction_pin].write(1)    # вращаем вперед
        board.digital[self._pull_force_pin].write(1)        # на полную катушку!

    def reverse(self):
        board = self._get_board()
        board.digital[self._pull_direction_pin].write(0)    # вращаем назад
        board.digital[self._pull_force_pin].write(1)        # на полную катушку!

    def stop(self):
        board = self._get_board()
        board.digital[self._pull_direction_pin].write(0)
        board.digital[self._pull_force_pin].write(0)

    def left(self):
        board = self._get_board()
        board.digital[self._rudder_direction_pin].write(0)
        board.digital[self._rudder_force_pin].write(1)

    def right(self):
        board = self._get_board()
        board.digital[self._rudder_direction_pin].write(1)
        board.digital[self._rudder_force_pin].write(1)

    def center(self):
        board = self._get_board()
        board.digital[self._rudder_direction_pin].write(0)
        board.digital[self._rudder_force_pin].write(0)

#
# def forward(rate=100):
#     pwm_b.start(0)
#     GPIO.output(settings.IN_3, False)
#     GPIO.output(settings.IN_4, True)
#     pwm_b.start(rate)
#
#
# def reverse(rate=100):
#     pwm_b.start(0)
#     GPIO.output(settings.IN_3, True)
#     GPIO.output(settings.IN_4, False)
#     pwm_b.start(rate)
#
#
# def stop():
#     pwm_b.start(0)
#     GPIO.output(settings.IN_3, False)
#     GPIO.output(settings.IN_4, False)
#     # pwm_b.start(100)
#
#
# def left(rate=100):
#     pwm_a.start(0)
#     GPIO.output(settings.IN_1, False)
#     GPIO.output(settings.IN_2, True)
#     pwm_a.start(rate)
#
#
# def right(rate=100):
#     pwm_a.start(0)
#     GPIO.output(settings.IN_1, True)
#     GPIO.output(settings.IN_2, False)
#     pwm_a.start(rate)
#
#
# def center():
#     pwm_a.start(0)
#     GPIO.output(settings.IN_1, False)
#     GPIO.output(settings.IN_2, False)
#     # pwm_a.start(100)
#
#
# def free():
#     pwm_a.start(0)
#     pwm_b.start(0)
#     GPIO.output(settings.IN_1, False)
#     GPIO.output(settings.IN_2, False)
#     GPIO.output(settings.IN_3, False)
#     GPIO.output(settings.IN_4, False)
#
#
# def photo():
#     with picamera.PiCamera() as camera:
#         camera.capture('tmp.jpg')
