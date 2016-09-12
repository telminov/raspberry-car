from time import sleep
import datetime
from django.core.management.base import BaseCommand
from core import models, consts
from django.utils import timezone
import core.car
import RPi.GPIO as GPIO


class Command(BaseCommand):
    args = ''
    help = 'Look for non-fulfillment of the command to the database and executes them if they are not overdue'

    def move(self):
        now = timezone.now()
        deadline = now - datetime.timedelta(seconds=1)
        qs = models.Command.objects.filter(name__in=consts.MOVE_COMMANDS, dm__gte=deadline)

        if qs:
            latest = qs[0]
            value = int(latest.value or 100)
            if latest.name == consts.FORWARD:
                core.car.forward(value)
            elif latest.name == consts.REVERSE:
                core.car.reverse(value)
            elif latest.name == consts.STOP:
                core.car.stop()
        else:
            core.car.stop()

    def action(self):
        now = timezone.now()
        deadline = now - datetime.timedelta(seconds=1)
        qs = models.Command.objects.filter(name__in=consts.ACTION_COMMANDS, dm__gte=deadline)

        if qs:
            latest = qs[0]
            if latest.name == consts.LEFT:
                core.car.left()
            elif latest.name == consts.RIGHT:
                core.car.right()
            elif latest.name == consts.CENTER:
                core.car.center()
        else:
            core.car.center()

    def handle(self, *args, **options):
        try:
            while True:
                self.move()
                self.action()
                sleep(0.25)
        finally:
            GPIO.cleanup()


