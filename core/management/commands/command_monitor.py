from time import sleep
import datetime
from django.core.management.base import BaseCommand
from core import models, consts
from django.utils import timezone
import RPi.GPIO as GPIO

from django.conf import settings

if settings.CAR_TYPE == 'tank':
    from core.tank import left, forward, center, reverse, stop, free, right
else:
    from core.car import left, forward, center, reverse, stop, free, right


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
                forward(value)
            elif latest.name == consts.REVERSE:
                reverse(value)
            elif latest.name == consts.STOP:
                stop()
        else:
            stop()

    def action(self):
        now = timezone.now()
        deadline = now - datetime.timedelta(seconds=1)
        qs = models.Command.objects.filter(name__in=consts.ACTION_COMMANDS, dm__gte=deadline)

        if qs:
            latest = qs[0]
            if latest.name == consts.LEFT:
                left()
            elif latest.name == consts.RIGHT:
                right()
            elif latest.name == consts.CENTER:
                center()
        else:
            if settings.CAR_TYPE == 'car':
                center()

    def handle(self, *args, **options):
        try:
            while True:
                self.move()
                self.action()
                sleep(0.25)
        finally:
            GPIO.cleanup()


