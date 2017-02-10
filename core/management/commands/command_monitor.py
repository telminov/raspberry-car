from time import sleep
import datetime
from django.core.management.base import BaseCommand
from core import models, consts
from django.utils import timezone
from django.conf import settings
from core.car import Car


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
                # self.car.forward(value)
                self.car.forward()
            elif latest.name == consts.REVERSE:
                # reverse(value)
                self.car.reverse()
            elif latest.name == consts.STOP:
                self.car.stop()
        else:
            self.car.stop()

    def action(self):
        now = timezone.now()
        deadline = now - datetime.timedelta(seconds=1)
        qs = models.Command.objects.filter(name__in=consts.ACTION_COMMANDS, dm__gte=deadline)

        if qs:
            latest = qs[0]
            if latest.name == consts.LEFT:
                self.car.left()
            elif latest.name == consts.RIGHT:
                self.car.right()
            elif latest.name == consts.CENTER:
                self.car.center()
        else:
            if settings.CAR_TYPE == 'car':
                self.car.center()

    def handle(self, *args, **options):
        self.car = Car()

        while True:
            self.move()
            self.action()
            sleep(0.25)
