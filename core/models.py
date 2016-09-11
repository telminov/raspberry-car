from django.db import models
from . import consts


class Command(models.Model):
    name = models.CharField(max_length=15, unique=True, choices=consts.COMMAND_CHOICES)
    dm = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        ordering = '-dm',

    def __str__(self):
        return self.name

