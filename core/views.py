from django.conf import settings
from django.utils.timezone import now
from rest_framework import views
from rest_framework import response
from core import models
from core import serializers


class Index(views.APIView):
    def get(self, request, *args, **kwargs):
        return response.Response({'name': settings.CAR_NAME})
index = Index.as_view()


class Command(views.APIView):
    queryset = models.Command.objects.all()
    serializer_class = serializers.Command

    def post(self, request, *args, **kwargs):
        serializer = serializers.Command(data=request.data)
        serializer.is_valid(raise_exception=True)

        command_name = serializer.validated_data['name']
        qs = models.Command.objects.filter(name=command_name)
        if qs.exists():
            qs.update(dm=now())
        else:
            models.Command.objects.create(name=command_name, dm=now())

        return response.Response({'result': 'ok'})

command = Command.as_view()
