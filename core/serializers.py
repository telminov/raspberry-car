# coding: utf-8
from rest_framework import serializers
from core import models


class Command(serializers.ModelSerializer):
    class Meta:
        model = models.Command
