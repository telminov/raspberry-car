# coding: utf-8
from django import http
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

XS_SHARING_ALLOWED_ORIGINS = getattr(settings, 'XS_SHARING_ALLOWED_ORIGINS', '*')
XS_SHARING_ALLOWED_METHODS = getattr(settings, 'XS_SHARING_ALLOWED_METHODS', ['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE'])
XS_SHARING_ALLOWED_HEADERS = getattr(settings, 'XS_SHARING_ALLOWED_HEADERS', ['Content-Type', '*'])
XS_SHARING_ALLOWED_CREDENTIALS = getattr(settings, 'XS_SHARING_ALLOWED_CREDENTIALS', 'true')


class XsSharing(MiddlewareMixin):
    """
    This middleware allows cross-domain XHR using the html5 postMessage API.

    Access-Control-Allow-Origin: http://foo.example
    Access-Control-Allow-Methods: POST, GET, OPTIONS, PUT, DELETE

    Based off https://gist.github.com/426829
    """
    def process_request(self, request):
        if 'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META:
            response = http.HttpResponse()
            if settings.DEBUG and 'HTTP_ORIGIN' in request.META:
                response['Access-Control-Allow-Origin'] = request.META['HTTP_ORIGIN']
            else:
                response['Access-Control-Allow-Origin'] = XS_SHARING_ALLOWED_ORIGINS
            response['Access-Control-Allow-Methods'] = ",".join( XS_SHARING_ALLOWED_METHODS )
            response['Access-Control-Allow-Headers'] = ",".join( XS_SHARING_ALLOWED_HEADERS )
            response['Access-Control-Allow-Credentials'] = XS_SHARING_ALLOWED_CREDENTIALS
            return response

        return None

    def process_response(self, request, response):
        if settings.DEBUG and 'HTTP_ORIGIN' in request.META:
            response['Access-Control-Allow-Origin'] = request.META['HTTP_ORIGIN']
        else:
            response['Access-Control-Allow-Origin'] = XS_SHARING_ALLOWED_ORIGINS
        response['Access-Control-Allow-Methods'] = ",".join( XS_SHARING_ALLOWED_METHODS )
        response['Access-Control-Allow-Headers'] = ",".join( XS_SHARING_ALLOWED_HEADERS )
        response['Access-Control-Allow-Credentials'] = XS_SHARING_ALLOWED_CREDENTIALS

        return response