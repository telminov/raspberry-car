# coding: utf-8
from django.conf.urls import url
import core.views

urlpatterns = [
    url(r'command/$', core.views.command),
]
